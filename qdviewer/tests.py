db654 = QgsVectorLayer("D:\TTSIB\ESS\EXPORT\DB000654.DBF", "db654", "ogr")
db695   = QgsVectorLayer("D:\TTSIB\ESS\EXPORT\DB000695.DBF", "db695", "ogr")
db142    = QgsVectorLayer("D:\TTSIB\ESS\EXPORT\DB000142.DBF", "db142", "ogr")
QgsVectorFileWriter.writeAsVectorFormat(db654, "D:\TTSIB\ESS\EXPORT\db12.sqlite", "utf-8", QgsCoordinateReferenceSystem(), "SQLite", False, ['layername=db654'])
QgsVectorFileWriter.writeAsVectorFormat(db695, "D:\TTSIB\ESS\EXPORT\db12.sqlite", "utf-8", QgsCoordinateReferenceSystem(), "SQLite", False, ['layername=db695'])
QgsVectorFileWriter.writeAsVectorFormat(db142, "D:\TTSIB\ESS\EXPORT\db12.sqlite", "utf-8", QgsCoordinateReferenceSystem(), "SQLite", False, ['layername=db142'])