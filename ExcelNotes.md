# Files modified:
### xl/worksheets/sheet1.xml:
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
  xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
  xmlns:x14ac="http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac" mc:Ignorable="x14ac">
  <dimension ref="A1"/>
  <sheetViews>
    <sheetView tabSelected="1" workbookViewId="0"/>
  </sheetViews>
  <sheetFormatPr defaultRowHeight="15" x14ac:dyDescent="0.25"/>
  <sheetData/>
  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3"/>
  <drawing r:id="rId1"/>
</worksheet>
```

<strong>Modified line:<strong>

```xml
<drawing r:id="rId1"/>
```

### [Content_Types].xml:
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
    <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
    <Override PartName="/xl/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
    <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
    <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
    <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
    <Override PartName="/xl/drawings/drawing1.xml" ContentType="application/vnd.openxmlformats-officedocument.drawing+xml"/>
</Types>
```

<strong>Modified line:<strong>
```xml
<Override PartName="/xl/drawings/drawing1.xml" ContentType="application/vnd.openxmlformats-officedocument.drawing+xml"/>
```

# Files added:
### xl/drawings/drawing1.xml:
```xml
<xdr:wsDr xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing"
    xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
    <xdr:twoCellAnchor editAs="oneCell">
        <xdr:from>
            <xdr:col>0</xdr:col>
            <xdr:colOff>1</xdr:colOff>
            <xdr:row>0</xdr:row>
            <xdr:rowOff>1</xdr:rowOff>
        </xdr:from>
        <xdr:to>
            <xdr:col>0</xdr:col>
            <xdr:colOff>0</xdr:colOff>
            <xdr:row>0</xdr:row>
            <xdr:rowOff>0</xdr:rowOff>
        </xdr:to>
        <xdr:pic>
            <xdr:nvPicPr>
                <xdr:cNvPr id="1" name="Picture 1"/>
                <xdr:cNvPicPr>
                    <a:picLocks noChangeAspect="1"/>
                </xdr:cNvPicPr>
            </xdr:nvPicPr>
            <xdr:blipFill>
                <a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:link="rId4"/>
                <a:stretch>
                    <a:fillRect/>
                </a:stretch>
            </xdr:blipFill>
            <xdr:spPr>
                <a:xfrm>
                    <a:off x="0" y="0"/>
                    <a:ext cx="0" cy="0"/>
                </a:xfrm>
                <a:prstGeom prst="rect">
                    <a:avLst/>
                </a:prstGeom>
            </xdr:spPr>
        </xdr:pic>
        <xdr:clientData/>
    </xdr:twoCellAnchor>
</xdr:wsDr>
```

        
### xl/drawings/_rels/drawing1.xml.rels:
```xml
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship TargetMode="External" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Id="rId4" Target="REPLACEMENTURI"/>
</Relationships>
```

### xl/worksheets/_rels/sheet1.xml.rels:
```xml
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/drawing" Id="rId1" Target="../drawings/drawing1.xml"/>
</Relationships>
```



# Mutually-dependent files:
- [xl/worksheets/sheet1.xml] [xl/worksheets/rels/sheet1.xml.rels] 
- [xl/drawings/drawing1.xml] [xl/drawings/_rels/drawing1.xml.rels] [[Content_Types].xml]
    