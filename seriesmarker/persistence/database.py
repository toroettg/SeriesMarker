#==============================================================================
# -*- coding: utf-8 -*-
# 
# Copyright (C) 2013 Tobias Röttger <toroettg@gmail.com>
# 
# This file is part of SeriesMarker.
# 
# SeriesMarker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
# 
# SeriesMarker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with SeriesMarker.  If not, see <http://www.gnu.org/licenses/>.
#==============================================================================

from seriesmarker.persistence.exception import EntityExistsException, EntityNotFoundException
from seriesmarker.util import config
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import sessionmaker
import errno
import logging
import os

logger = logging.getLogger(__name__)

Base = declarative_base()
db_engine = None
db_session = scoped_session(sessionmaker(autoflush=False, autocommit=False))

# Imports for Metadata creation
from seriesmarker.persistence.model.banner import Banner  # @UnusedImport
from seriesmarker.persistence.model.banner_extra import BannerExtra  # @UnusedImport
from seriesmarker.persistence.model.role import Role  # @UnusedImport
from seriesmarker.persistence.model.role_extra import RoleExtra  # @UnusedImport
from seriesmarker.persistence.model.director import Director  # @UnusedImport
from seriesmarker.persistence.model.writer import Writer  # @UnusedImport
from seriesmarker.persistence.model.season import Season  # @UnusedImport
from seriesmarker.persistence.model.guest import Guest  # @UnusedImport
from seriesmarker.persistence.model.episode import Episode  # @UnusedImport
from seriesmarker.persistence.model.episode_extra import EpisodeExtra  # @UnusedImport
from seriesmarker.persistence.model.series_extra import SeriesExtra  # @UnusedImport
from seriesmarker.persistence.model.actor import Actor  # @UnusedImport
from seriesmarker.persistence.model.genre import Genre  # @UnusedImport
from seriesmarker.persistence.model.series import Series


def db_init():
    """Initializes the database.
    
    Creates or connects to a database at a location, specified by the configuration file.
    
    .. seealso:: :mod:`.config`
    
    """
    global db_engine, db_session

    logger.info("Initializing database '{db_name}' in '{db_location}'".format(db_name=config.application_name, db_location=config.dirs.user_data_dir))

    try:
        os.makedirs(config.dirs.user_data_dir)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise

    db_URL = 'sqlite:///{db_location}{sep}{db_name}.db'.format(db_location=config.dirs.user_data_dir, sep=os.sep, db_name=config.application_name)

    db_engine = create_engine(db_URL, echo=False)

    db_session.configure(bind=db_engine)

    Base.metadata.create_all(bind=db_engine)

def db_commit():
    """Writes pending changes to the database."""
    db_session.commit()

def db_add_series(series):
    """Adds a new series to the database.
    
    :param series: The series to add.
    :type series: :class:`.Series`
    :raises: :exc:`.EntityExistsException`
    
    """
    try:
        db_session.query(Series).filter_by(id=series.id).one()
    except NoResultFound:
        db_session.add(series)
        db_session.commit()
        logger.info("Added series '{series}'".format(series=series.series_name))
    else:
        raise EntityExistsException(series.id, series.__tablename__)

def db_remove_banner(banner):
    """Removes a given banner from the database.
    
    :param banner: The banner to remove.
    :type banner: :class:`.Banner`
    
    """
    db_session.delete(banner.extra)
    db_session.delete(banner)
    logging.debug("Removed {banner}".format(banner=banner))

def db_remove_item(item):
    """Removes a generic (atomic) item from the database.

    .. todo:: Check if item really is generic, dispatch to proper remove function otherwise.
    
    :param item: The item to remove.

    """
    db_session.delete(item)

def db_get_series(series_id=None):
    """Queries the database for series.
    
    :param series_id: The ID of the series to retrieve.
    :type series_id: Integer or None
    :returns: The :class:`.Series` related to the given ID or None if no entry matches the ID.
    :returns: A list of all :class:`.Series` in the database if no ID is specified (may be empty).
    
    """
    if series_id == None:
        return db_session.query(Series).all()
    else:
        try:
            return db_session.query(Series).filter_by(id=series_id).one()
        except NoResultFound:
            return None

def db_remove_episode(episode):
    """Removes a given episode from the database.
    
    :param episode: The episode to remove.
    :type episode: :class:`.Episode`
    
    """
    for director in episode.directors:
        db_session.delete(director)

    for writer in episode.writers:
        db_session.delete(writer)

    for guest in episode.guests:
        db_session.delete(guest)

    db_session.delete(episode.extra)

    db_session.delete(episode)

    logging.debug("Removed {episode}".format(episode=episode))

def db_remove_season(season):
    """Removes a given season from the database.
    
    :param season: The season to remove.
    :type season: :class:`.Season`
    
    """
    for episode in season.episodes:
        db_remove_episode(episode)

    if season.banner != None:
        db_remove_banner(season.banner)

    db_session.delete(season)

    logging.debug("Removed {season}".format(season=season))

def db_remove_role(role):
    """Removes a given role from the database.
    
    :param role: The role to remove.
    :type role: :class:`.Role`
    
    """
    db_session.delete(role.extra)
    db_session.delete(role)

def db_remove_series(series):
    """Removes a given series from the database.
    
    :param series: The series to remove.
    :type series: :class:`.Series`
    :raises: :exc:`.EntityNotFoundException`
    
    """
    try:
        db_session.query(Series).filter_by(id=series.id).one()
    except NoResultFound:
        raise EntityNotFoundException(series.id, series.__tablename__)
    else:
        for season in series.seasons:
            db_remove_season(season)

        for actor in series.actors:
                db_session.delete(actor)

        for genre in series.genre:
                db_session.delete(genre)

        for role in series.extra.roles:
            db_session.delete(role.extra)
            db_session.delete(role)

        if series.extra.banner != None:
            db_remove_banner(series.extra.banner)

        db_session.delete(series.extra)

        db_session.delete(series)

        db_session.commit()

        logging.info("Removed series '{series}'".format(series=series.series_name))
