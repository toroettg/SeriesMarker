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

from PySide.QtGui import QPixmap, QPixmapCache
from PySide.QtCore import Qt
from seriesmarker.net.banner_loader import banner_loader

pixmap_cache = QPixmapCache()

class DecoratedNode(object):
    """Class to handle the decoration of nodes with banners."""
    def __init__(self, scale=None, cache=True):
        """Initializes a new instance.
        
        Also defines if and to which size a banner should be scaled to
        and if the banner should be cached for further usage.
        
        :param scale: Defines the size to scale a banner to if given.
        :type scale: :class:`.PySide.QtCore.QSize`
        :param cache: Defines whether or not a loaded banner should be
            cached on disk.
        :type cache: bool
        
        """
        super().__init__()

        self._scale = scale
        self._cache = cache

    def banner_url(self):
        """Describes a unique string for banner identification. 
        
        :returns: The URL of the node's banner.
        
        """
        return None

    def decoration(self, index):
        """Defines the decoration of the node.
        
        Tries to load a banner from the URL, defined by :py:meth:`banner_url`,
        sets a default image while loading and in case the attempt to
        obtain a banner was unsuccesful. If a banner has been cached for the
        given URL, the cached image will be used instead.
        
        :param index: The index referring to the node to get decoration for.
        :type index: :class:`.PySide.QtCore.QModelIndex`
        
        :returns: The :class:`PySide.QtGui.Pixmap` to use as the node's decoration.
        
        """
        pixmap = QPixmap()
        banner_url = self.banner_url()
        if banner_url:
            placeholder = ":/icons/image-loading.png"
            fetch = True
        else:
            banner_url = placeholder = ":/icons/image-missing.png"
            fetch = False

        if not pixmap_cache.find(banner_url, pixmap):
            if fetch:
                banner_loader.fetch_banner(banner_url, index, self._cache)
            pixmap.load(placeholder)
            if self._scale:
                pixmap = pixmap.scaled(self._scale, Qt.AspectRatioMode.KeepAspectRatio)
            pixmap_cache.insert(banner_url, pixmap)
        return pixmap

    def banner_loaded(self, pixmap):
        """Adds a banner, loaded by :class:`.BannerLoader`, to the cache.
        
        If a scale size was given while initialization, also scales the
        banner before adding it to the cache.
        
        :param pixmap: The pixmap containing the banner to cache. 
        :type pixmap: :class:`PySide.QtGui.Pixmap`
        
        """
        if self._scale:
            pixmap = pixmap.scaled(self._scale, Qt.AspectRatioMode.KeepAspectRatio)
        pixmap_cache.insert(self.banner_url(), pixmap)
