# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ForestComplexesGenerator
                                 A QGIS plugin
 Plugin for create merged forest complexes by declared distance between single polygons
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-03-22
        copyright            : (C) 2023 by BULiGL
        email                : borys.draus@zarzad.buligl.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ForestComplexesGenerator class from file ForestComplexesGenerator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .forest_complexes_generator import ForestComplexesGenerator
    return ForestComplexesGenerator(iface)
