// Adafruit Feather RP2040
// Params
//  mounting: default is false
//		if true, will add through holes sized for the Feather

module.exports = {
  params: {
    VBAT: { type: "net", value: "VBAT" },
    EN: { type: "net", value: "EN" },
    VBUS: { type: "net", value: "VBUS" },
    D13: { type: "net", value: "D13" },
    D12: { type: "net", value: "D12" },
    D11: { type: "net", value: "D11" },
    D10: { type: "net", value: "D10" },
    D9: { type: "net", value: "D9" },
    D6: { type: "net", value: "D6" },
    D5: { type: "net", value: "D5" },
    SCL: { type: "net", value: "SCL" },
    SDA: { type: "net", value: "SDA" },
    RST: { type: "net", value: "RST" },
    V33: { type: "net", value: "V33" },
    GND: { type: "net", value: "GND" },
    A0: { type: "net", value: "A0" },
    A1: { type: "net", value: "A1" },
    A2: { type: "net", value: "A2" },
    A3: { type: "net", value: "A3" },
    D24: { type: "net", value: "D24" },
    D25: { type: "net", value: "D25" },
    SCK: { type: "net", value: "SCK" },
    MOSI: { type: "net", value: "MOSI" },
    MISO: { type: "net", value: "MISO" },
    RX: { type: "net", value: "RX" },
    TX: { type: "net", value: "TX" },
    D4: { type: "net", value: "D4" },
    class: "MCU",
    mounting: false,
    outline: false,
  },
  body: (p) => {
    const standard = `
			(module Feather_RP2040 (layer F.Cu)
			${p.at /* parametric position */}
	
			${"" /* footprint reference */}
			(fp_text reference "${p.ref}" (at 0 0) (layer F.SilkS) ${
      p.ref_hide
    } (effects (font (size 1.27 1.27) (thickness 0.15))))
			(fp_text value "" (at 0 0) (layer F.SilkS) hide (effects (font (size 1.27 1.27) (thickness 0.15))))

			${"" /* usb port */}
	
			(fp_line (start -26.5 -4.6) (end -26.5 4.6)(layer Dwgs.User )(width 0.15))
			(fp_line (start -18.7 -4.6) (end -26.5 -4.6)(layer Dwgs.User )(width 0.15))
			(fp_line (start -18.7 -4.6) (end -18.7 4.6)(layer Dwgs.User )(width 0.15))
			(fp_line (start -18.7 4.6) (end -26.5 4.6)(layer Dwgs.User )(width 0.15))


			${"" /* component outline */}
			(fp_line (start -25.4 11.43) (end 25.4 11.43) (layer Dwgs.User) (width 0.15))
			(fp_line (start 25.4 11.43) (end 25.4 -11.43) (layer Dwgs.User) (width 0.15))
			(fp_line (start 25.4 -11.43) (end -25.4 -11.43) (layer Dwgs.User) (width 0.15))
			(fp_line (start -25.4 -11.43) (end -25.4 11.43) (layer Dwgs.User) (width 0.15))
		`

    const mounting = `
			${"" /* mounting holes */}
			(pad "" np_thru_hole circle (at -22.86 8.89) (size 3.81 3.81) (drill 2.54) (layers *.Cu *.Mask))
			(pad "" np_thru_hole circle (at 22.86 8.89) (size 3.81 3.81) (drill 2.54) (layers *.Cu *.Mask))
			(pad "" np_thru_hole circle (at -22.86 -8.89) (size 3.81 3.81) (drill 2.54) (layers *.Cu *.Mask))
			(pad "" np_thru_hole circle (at 22.86 -8.89) (size 3.81 3.81) (drill 2.54) (layers *.Cu *.Mask))
		`

    const pins = `
			${"" /* pin names */}
			(fp_text user VBAT (at -8.89 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user EN (at -6.35 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user VBUS (at -3.81 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D13 (at -1.27 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D12 (at 1.27 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D11 (at 3.81 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D10 (at 6.35 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D9 (at 8.89 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D6 (at 11.43 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D5 (at 13.97 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user SCL (at 16.51 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user SDA (at 19.05 -7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			
			(fp_text user RST (at -19.05 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user 3.3V (at -16.51 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user 3.3V (at -13.97 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user GND (at -11.43 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user A0 (at -8.89 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user A1 (at -6.35 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user A2 (at -3.81 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user A3 (at -1.27 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D24 (at 1.27 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D25 (at 3.81 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user SCK (at 6.35 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user MOSI (at 8.89 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user MISO (at 11.43 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user RX (at 13.97 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user TX (at 16.51 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
			(fp_text user D4 (at 19.05 7 ${p.rot + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
	
			${"" /* pins */}
			(pad 1 thru_hole circle (at -8.89 -10.16) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.VBAT})
			(pad 2 thru_hole circle (at -6.35 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.EN})
			(pad 3 thru_hole circle (at -3.81 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.VBUS})
			(pad 4 thru_hole circle (at -1.27 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D13})
			(pad 5 thru_hole circle (at 1.27 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D12})
			(pad 6 thru_hole circle (at 3.81 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D11})
			(pad 7 thru_hole circle (at 6.35 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D10})
			(pad 8 thru_hole circle (at 8.89 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D9})
			(pad 9 thru_hole circle (at 11.43 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D6})
			(pad 10 thru_hole circle (at 13.97 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D5})
			(pad 11 thru_hole circle (at 16.51 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.SCL})
			(pad 12 thru_hole circle (at 19.05 -10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.SDA})
			
			(pad 13 thru_hole circle (at -19.05 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.RST})
			(pad 14 thru_hole circle (at -16.51 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.V33})
			(pad 15 thru_hole circle (at -13.97 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.V33})
			(pad 16 thru_hole circle (at -11.43 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.GND})
			(pad 17 thru_hole circle (at -8.89 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.A0})
			(pad 18 thru_hole circle (at -6.35 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.A1})
			(pad 19 thru_hole circle (at -3.81 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.A2})
			(pad 20 thru_hole circle (at -1.27 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.A3})
			(pad 21 thru_hole circle (at 1.27 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D24})
			(pad 22 thru_hole circle (at 3.81 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D25})
			(pad 23 thru_hole circle (at 6.35 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.SCK})
			(pad 24 thru_hole circle (at 8.89 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.MOSI})
			(pad 25 thru_hole circle (at 11.43 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.MISO})
			(pad 26 thru_hole circle (at 13.97 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.RX})
			(pad 27 thru_hole circle (at 16.51 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.TX})
			(pad 28 thru_hole circle (at 19.05 10.16 0) (size 1.7526 1.7526) (drill 1.0922) (layers *.Cu *.Mask) ${p.D4})
		`

    return `
			${standard}
			${pins}
			${p.mounting ? mounting : ``})
		`
  },
}