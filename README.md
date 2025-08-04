`Some custom keyboards`

1. From within the directory for the corresponding layout run `ergogen .` to generate the output.
2. To convert jscad to stl use:
    `npx @jscad/cli@1 {INPUT} -of stla -o {OUTPUT}.stl`
3. Use `dxf-to-svg` to, well, convert ergogen's DXF files to SVG