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

from PySide.QtCore import QUrl, Slot, QObject, Qt
from PySide.QtGui import QPixmap
from PySide.QtNetwork import QNetworkAccessManager, QNetworkDiskCache, \
    QNetworkRequest, QNetworkReply
from seriesmarker.util.config import dirs
import logging

logger = logging.getLogger(__name__)

class BannerLoader(QObject):
    """Class to load banner from the net."""

    def __init__(self):
        """Creates a new instance."""
        super().__init__()
        self._ready_signal = {}

    def fetch_banner(self, url, index, cache=True):
        """Creates a request to load a banner from the given URL.
        
        A request is defined by its URL and carried out asynchronously. 
        The result is stored on disk if caching is enabled. When a request
        has been completed, :py:meth:`.finished_request` will be invoked.
        
        :param url: The location of the banner to load.
        :type url: string
        :param index: The index referring to a :class:`.DecoratedNode`
            to fetch a banner for (origin of the request). Used to inform
            the node's model when the request was finished.
        :type index: :class:`.PySide.QtCore.QModelIndex`
        :param cache: Determines if the loaded banner should be cached on disk.
        :type cache: bool
        
        """
        request = QNetworkRequest(QUrl(url))
        request.setAttribute(QNetworkRequest.CacheLoadControlAttribute, QNetworkRequest.PreferCache)
        request.setAttribute(QNetworkRequest.CacheSaveControlAttribute, cache)

        reply = access_manager.get(request)

        self._ready_signal[url] = index

        from_cache = bool(reply.attribute(QNetworkRequest.SourceIsFromCacheAttribute))
        logger.debug("Loading '{}' (Cached: {})".format(url, from_cache))

    @Slot(QNetworkReply)
    def finished_request(self, reply):
        """Processes replies and dispatches results to requesters.
        
        This method will be invoked on each finished request, submitted by
        :py:meth:`.fetch_banner`. It then converts the loaded data into a
        banner and passes the result on to the model of the request's origin.
        
        :param reply: The network reply from a banner load request.
        :type reply: :class:`.QNetworkReply`
        
        """
        pixmap = QPixmap()
        if reply.error() == QNetworkReply.NoError:
            image_bytes = reply.readAll()
            pixmap.loadFromData(image_bytes)
        else:
            pixmap.load(":/icons/image-missing.png")

        index = self._ready_signal.pop(reply.request().url().toString())

        index.model().setData(index, pixmap, Qt.DecorationRole)

banner_loader = BannerLoader()

disk_cache = QNetworkDiskCache()
disk_cache.setCacheDirectory(dirs.user_cache_dir)
disk_cache.setMaximumCacheSize(100 * 1024 * 1024)  # 100MB Cache

access_manager = QNetworkAccessManager()
access_manager.setCache(disk_cache)
access_manager.finished.connect(banner_loader.finished_request)
