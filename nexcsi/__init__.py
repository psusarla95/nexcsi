from nexcsi.decoder import decoder

# Indexes of Null and Pilot OFDM subcarriers
# https://www.oreilly.com/library/view/80211ac-a-survival/9781449357702/ch02.html
nulls = {
    20: [x+32 for x in [
        -32, -31, -30, -29,
              31,  30,  29,  0
    ]],

    40: [x+64 for x in [
        -64, -63, -62, -61, -60, -59, -1, 
              63,  62,  61,  60,  59,  1,  0
    ]],

    80: [x+128 for x in [
        -128, -127, -126, -125, -124, -123, -1,
               127,  126,  125,  124,  123,  1,  0
    ]],

    160: [x+256 for x in [
        -256, -255, -254, -253, -252, -251, -129, -128, -127, -5, -4, -3, -2, -1,
               255,  254,  253,  252,  251,  129,  128,  127,  5,  4,  3,  3,  1,  0 
    ]]
}

pilots = {
    20: [x+32 for x in [
        -21, -7,
         21,  7
    ]],

    40: [x+64 for x in [
        -53, -25, -11, 
         53,  25,  11
    ]],

    80: [x+128 for x in [
        -103, -75, -39, -11,
         103,  75,  39,  11
    ]],

    160: [x+256 for x in [
        -231, -203, -167, -139, -117, -89, -53, -25,
         231,  203,  167,  139,  117,  89,  53,  25
    ]]
}