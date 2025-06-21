function board_extrude_2_outline_fn(){
    return new CSG.Path2D([[45.1007629,-135.3332748],[54.338846,-82.9415025]]).appendArc([57.8142138,-80.5080237],{"radius":3,"clockwise":true,"large":false}).appendPoint([75.5587932,-83.6368719]).appendArc([78.9754452,-81.4665904],{"radius":3,"clockwise":false,"large":false}).appendPoint([80.907393,-74.3322241]).appendArc([84.6300126,-72.2325808],{"radius":3,"clockwise":true,"large":false}).appendPoint([100.7983577,-76.8687792]).appendArc([104.4435421,-75.0132654],{"radius":3,"clockwise":false,"large":false}).appendPoint([105.4842448,-72.1609211]).appendArc([109.3285773,-70.3701144],{"radius":3,"clockwise":true,"large":false}).appendPoint([127.7363033,-77.0699787]).appendArc([129.551688,-80.8514443],{"radius":3,"clockwise":true,"large":false}).appendPoint([128.9110162,-82.7430248]).appendArc([130.8573789,-86.5687719],{"radius":3,"clockwise":false,"large":false}).appendPoint([162.3358088,-96.4088864]).appendArc([164.1259736,-96.4088864],{"radius":3,"clockwise":false,"large":false}).appendPoint([195.6044034,-86.5687719]).appendArc([197.5507662,-82.7430247],{"radius":3,"clockwise":false,"large":false}).appendPoint([196.9415728,-80.9443842]).appendArc([198.8502537,-77.1306897],{"radius":3,"clockwise":true,"large":false}).appendPoint([217.4807622,-71.035985]).appendArc([221.2317139,-72.8587883],{"radius":3,"clockwise":true,"large":false}).appendPoint([222.0181029,-75.0135613]).appendArc([225.6632026,-76.8688429],{"radius":3,"clockwise":false,"large":false}).appendPoint([241.8317698,-72.2325808]).appendArc([245.5543894,-74.3322241],{"radius":3,"clockwise":true,"large":false}).appendPoint([247.4863372,-81.4665904]).appendArc([250.9029892,-83.6368719],{"radius":3,"clockwise":false,"large":false}).appendPoint([268.6475686,-80.5080237]).appendArc([272.1229365,-82.9415024],{"radius":3,"clockwise":true,"large":false}).appendPoint([281.3610195,-135.3332748]).appendArc([278.9275409,-138.8086426],{"radius":3,"clockwise":true,"large":false}).appendPoint([258.6843611,-142.3780614]).appendArc([255.2408655,-140.1009088],{"radius":3,"clockwise":true,"large":false}).appendPoint([253.7532425,-133.681536]).appendArc([250.0037793,-131.4750215],{"radius":3,"clockwise":false,"large":false}).appendPoint([234.342764,-135.9657454]).appendArc([232.282909,-139.6659709],{"radius":3,"clockwise":false,"large":false}).appendPoint([237.3297945,-157.5107313]).appendArc([235.8588047,-160.9720865],{"radius":3,"clockwise":true,"large":false}).appendPoint([184.82244,-188.2909765]).appendArc([181.4170282,-187.8913578],{"radius":3,"clockwise":true,"large":false}).appendPoint([165.2205257,-173.5390771]).appendArc([161.2412567,-173.5390771],{"radius":3,"clockwise":false,"large":false}).appendPoint([145.0447543,-187.8913577]).appendArc([141.6393423,-188.2909765],{"radius":3,"clockwise":true,"large":false}).appendPoint([90.6029777,-160.9720866]).appendArc([89.1319879,-157.5107313],{"radius":3,"clockwise":true,"large":false}).appendPoint([94.1788734,-139.6659709]).appendArc([92.1190184,-135.9657454],{"radius":3,"clockwise":false,"large":false}).appendPoint([76.4580031,-131.4750216]).appendArc([72.7085399,-133.6815359],{"radius":3,"clockwise":false,"large":false}).appendPoint([71.2209169,-140.1009088]).appendArc([67.7774213,-142.3780614],{"radius":3,"clockwise":true,"large":false}).appendPoint([47.5342416,-138.8086426]).appendArc([45.1007628,-135.3332747],{"radius":3,"clockwise":true,"large":false}).close().innerToCAG()
.extrude({ offset: [0, 0, 2] });
}




                function bottom_case_fn() {
                    

                // creating part 0 of case bottom
                let bottom__part_0 = board_extrude_2_outline_fn();

                // make sure that rotations are relative
                let bottom__part_0_bounds = bottom__part_0.getBounds();
                let bottom__part_0_x = bottom__part_0_bounds[0].x + (bottom__part_0_bounds[1].x - bottom__part_0_bounds[0].x) / 2
                let bottom__part_0_y = bottom__part_0_bounds[0].y + (bottom__part_0_bounds[1].y - bottom__part_0_bounds[0].y) / 2
                bottom__part_0 = translate([-bottom__part_0_x, -bottom__part_0_y, 0], bottom__part_0);
                bottom__part_0 = rotate([0,0,0], bottom__part_0);
                bottom__part_0 = translate([bottom__part_0_x, bottom__part_0_y, 0], bottom__part_0);

                bottom__part_0 = translate([0,0,0], bottom__part_0);
                let result = bottom__part_0;
                
            
                    return result;
                }
            
            
        
            function main() {
                return bottom_case_fn();
            }

        