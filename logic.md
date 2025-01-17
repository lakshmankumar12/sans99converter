
Categories of letters

* vowel                 VWL
* mod-1                 MOD1
* mod-2                 MOD2
* mod-3                 MOD3
* sinble-consonant      SINC
* combo-consonant       CMBC
* half-consonant        HLFC
* vowelized-consonant   VWLC
* indep-symbol          INDP
* i                     SYMI
* R                     SYMR

Current-state

 Empty                         S_EMP
 Vowel                         S_VWL
 Vowel,mod-2                   S_VWLMOD2
 half-consonants(one or more)  S_HLFMORE
 plain-consonant               S_PLNCONS
 cons-mod1                     S_CONMOD1
 cons-mod2                     S_CONMOD2
 i-wait-on-empty               S_IWAIT
 i-wait-with-half              S_HLFMORE_AND_I


  » S_EMP
  » S_VWL
  » S_VWLMOD2
  » S_HLFMORE
  » S_PLNCONS
  » S_CONMOD1
  » S_CONMOD2
  » S_IWAIT
  » S_HLFMORE_AND_I



Action matrix

» VWL
  » S_EMP
    » current-add,  S_VWL
  » S_VWL
    » flush-prev, current-add, S_VWL
  » S_VWLMOD2
    » flush-prev, current-add, S_VWL
  » S_HLFMORE
    » error
  » S_PLNCONS
    » flush-prev, current-add, S_VWL
  » S_CONMOD1
    » flush-prev, current-add, S_VWL
  » S_CONMOD2
    » flush-prev, current-add, S_VWL
  » S_IWAIT
    » error
  » S_HLFMORE_AND_I
    » error
MOD1
  » S_EMP
    » error
  » S_VWL
    » error
  » S_VWLMOD2
    » error
  » S_HLFMORE
    » error
  » S_PLNCONS
    » current-add, S_CONMOD1
  » S_CONMOD1
    » error
  » S_CONMOD2
    » error
  » S_IWAIT
    » error
  » S_HLFMORE_AND_I
    » error
MOD2
  » S_EMP
    » error
  » S_VWL
    » current-add, S_VWLMOD2
  » S_VWLMOD2
    » error
  » S_HLFMORE
    » error
  » S_PLNCONS
    » current-add, S_CONMOD2
  » S_CONMOD1
    » current-add, S_CONMOD2
  » S_CONMOD2
    » error
  » S_IWAIT
    » error
  » S_HLFMORE_AND_I
    » error
MOD3
  » S_EMP
    » error
  » S_VWL
    » current-add-flush, S_EMP
  » S_VWLMOD2
    » current-add-flush, S_EMP
  » S_HLFMORE
    » error
  » S_PLNCONS
    » current-add-flush, S_EMP
  » S_CONMOD1
    » current-add-flush, S_EMP
  » S_CONMOD2
    » current-add-flush, S_EMP
  » S_IWAIT
    » error
  » S_HLFMORE_AND_I
    » error
SINC
  » S_EMP
    » current-add, S_PLNCONS
  » S_VWL
    » flush-prev, current-add, S_PLNCONS
  » S_VWLMOD2
    » flush-prev, current-add, S_PLNCONS
  » S_HLFMORE
    » current-add, S_PLNCONS
  » S_PLNCONS
    » flush-prev, current-add, S_PLNCONS
  » S_CONMOD1
    » flush-prev, current-add, S_PLNCONS
  » S_CONMOD2
    » flush-prev, current-add, S_PLNCONS
  » S_IWAIT
    » add-con, then mod1, S_CONMOD1
  » S_HLFMORE_AND_I
    » add-con, then mod1, S_CONMOD1
CMBC
  » S_EMP
    » current-add, S_PLNCONS
  » S_VWL
    » flush-prev, current-add, S_PLNCONS
  » S_VWLMOD2
    » flush-prev, current-add, S_PLNCONS
  » S_HLFMORE
    » current-add, S_PLNCONS
  » S_PLNCONS
    » flush-prev, current-add, S_PLNCONS
  » S_CONMOD1
    » flush-prev, current-add, S_PLNCONS
  » S_CONMOD2
    » flush-prev, current-add, S_PLNCONS
  » S_IWAIT
    » add-con, then mod1, S_CONMOD1
  » S_HLFMORE_AND_I
    » add-con, then mod1, S_CONMOD1
HLFC
  » S_EMP
    » current-add, S_HLFMORE
  » S_VWL
    » flush-prev, current-add, S_HLFMORE
  » S_VWLMOD2
    » flush-prev, current-add, S_HLFMORE
  » S_HLFMORE
    » current-add, S_HLFMORE
  » S_PLNCONS
    » flush-prev, current-add, S_HLFMORE
  » S_CONMOD1
    » flush-prev, current-add, S_HLFMORE
  » S_CONMOD2
    » flush-prev, current-add, S_HLFMORE
  » S_IWAIT
    » current-add, S_HLFMORE_AND_I
  » S_HLFMORE_AND_I
    » current-add, S_HLFMORE_AND_I
VWLC
  » S_EMP
    » current-add, S_CONMOD1
  » S_VWL
    » flush-prev, current-add, S_CONMOD1
  » S_VWLMOD2
    » flush-prev, current-add, S_CONMOD1
  » S_HLFMORE
    » current-add, S_CONMOD1
  » S_PLNCONS
    » flush-prev, current-add, S_CONMOD1
  » S_CONMOD1
    » flush-prev, current-add, S_CONMOD1
  » S_CONMOD2
    » flush-prev, current-add, S_CONMOD1
  » S_IWAIT
    » error
  » S_HLFMORE_AND_I
    » error
INDP
  » S_EMP
    » current-add-flush, S_EMP
  » S_VWL
    » flush-prev, current-add-flush, S_EMP
  » S_VWLMOD2
    » flush-prev, current-add-flush, S_EMP
  » S_HLFMORE
    » error
  » S_PLNCONS
    » flush-prev, current-add-flush, S_EMP
  » S_CONMOD1
    » flush-prev, current-add-flush, S_EMP
  » S_CONMOD2
    » flush-prev, current-add-flush, S_EMP
  » S_IWAIT
    » error
  » S_HLFMORE_AND_I
    » error
SYMI
  » S_EMP
    » none, S_IWAIT
  » S_VWL
    » flush-prev, S_IWAIT
  » S_VWLMOD2
    » flush-prev, S_IWAIT
  » S_HLFMORE
    » error
  » S_PLNCONS
    » flush-prev, S_IWAIT
  » S_CONMOD1
    » flush-prev, S_IWAIT
  » S_CONMOD2
    » flush-prev, S_IWAIT
  » S_IWAIT
    » error
  » S_HLFMORE_AND_I
    » error
SYMR
  » S_EMP
    » error
  » S_VWL
    » error
  » S_VWLMOD2
    » error
  » S_HLFMORE
    » error
  » S_PLNCONS
    » add r-h at sart, S_PLNCONS
  » S_CONMOD1
    » add r-h at sart, S_CONMOD1
  » S_CONMOD2
    » add r-h at sart, S_CONMOD2
  » S_IWAIT
    » error
  » S_HLFMORE_AND_I
    » error
