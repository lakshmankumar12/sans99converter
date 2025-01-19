function barah_to_unicode()
{

var array_one = new Array(

"û" ,	"" , // ha, cha, Da, nga, ke baad khaalii sthaan
"ü" ,	"" , // ka, fa, kta kii bakulii
"ã" ,	"å" ,
"Á" ,	"ॐ" ,
"þ" ,	"॑" , // Udaatta
"ý" ,	"॒" , // Anudaatta
"Â" ,	"रु" ,
"Ã" ,	"रू" ,
"ÄQ" ,	"ड़" ,
"ÄR" ,	"ढ़" ,
"ÄT" ,	"फ़" ,
"Äe" ,	"ज़्" ,
"‚" ,	"क्क" ,
"ƒ¡" ,	"ङ्क" ,
"„¡" ,	"ङ्ख" ,
"…¡" ,	"ङ्ग" ,
"†¡" ,	"ङ्घ" ,
"‡¡" ,	"ङ्क्त" ,
"ˆ¡" ,	"ङ्ङ" ,
"‰¡" ,	"ङ्म" ,
"Š" ,	"च्च" ,
"‹" ,	"ज्ज" ,
"Œ" ,	"ड्ड" ,
"" ,	"ड्ढ" ,
"Ž" ,	"ड्य" ,
"" ,	"ट्ट" ,
"" ,	"ट्ठ" ,
"•" ,	"ड्ढ" ,
"–" ,	"ट्ट" ,
"—" ,	"ट्ठ" ,
"˜" ,	"ढ्ढ" ,
"™" ,	"हृ" ,
"š" ,	"ट्य" ,
"›" ,	"ठ्ठ" ,
"œ" ,	"ठ्य" ,
"" ,	"ढ्ढ" ,
"ž" ,	"ढ्य" ,
"Ÿ" ,	"द्र्य" ,
"¢" ,	"क्र" ,
"£" ,	"क्त" ,
"¤" ,	"क्ष्" ,
"¥" ,	"ज्ञ्" ,
"¦" ,	"त्न्" ,
"§" ,	"त्र्" ,
"¨" ,	"त्त्" ,
"©" ,	"द्म" ,
"ª" ,	"द्ग" ,
"«" ,	"द्घ" ,
"¬" ,	"द्द" ,
"®" ,	"द्ध" ,
"¯" ,	"द्ब" ,
"°" ,	"द्भ" ,
"±" ,	"द्य" ,
"²" ,	"द्व" ,
"³" ,	"न्न्" ,
"´" ,	"श्र्" ,
"µ" ,	"श्व्" ,
"μ" ,   "श्व" , // 21-9-2013
"¶" ,	"श्च्" ,
"·" ,	"ष्ट" , // 21-9-2013
"¸" ,	"ष्ठ" ,
"¹" ,	"ष्ट" ,
"º" ,	"ह्ण" ,
"»" ,	"ह्न" ,
"¼" ,	"ह्म" ,
"½" ,	"ह्य" ,
"¾" ,	"ह्र" ,
"¿" ,	"ह्ल" ,
"À" ,	"ह्व" ,
"ê" ,	"्र" ,
"ë" ,	"्र" ,
"ì" ,	"्र" ,
"í" ,	"्र" ,
"A" ,	"अ" ,
"B" ,	"ऑ" ,
"C" ,	"इ" ,
"D" ,	"ई" ,
"E" ,	"उ" ,
"F" ,	"ऊ" ,
"G" ,	"ऋ" ,
"H" ,	"ॠ" ,
"Lå" ,	"ऐ" ,
"L" ,	"ए" ,
"Y" ,	"क्" ,
"Z" ,	"ख्" ,
"a" ,	"ग्" ,
"b" ,	"घ्" ,
"M" ,	"क" ,
"X" ,	"ङ" ,
"c" ,	"च्" ,
"e" ,	"ज्" ,
"f" ,	"झ्" ,
"g" ,	"ञ्" ,
"N" ,	"छ" ,
"d" ,	"छ" ,
"O" ,	"ट" ,
"P" ,	"ठ" ,
"Q" ,	"ड" ,
"R" ,	"ढ" ,
"h" ,	"ण्" ,
"i" ,	"त्" ,
"j" ,	"थ्" ,
"k" ,	"ध्" ,
"l" ,	"न्" ,
"S" ,	"द" ,
"m" ,	"प्" ,
"n" ,	"फ्" ,
"o" ,	"ब्" ,
"p" ,	"भ्" ,
"q" ,	"म्" ,
"T" ,	"फ" ,
"r" ,	"य्" ,
"s" ,	"ल्" ,
"t" ,	"ळ्" ,
"u" ,	"व्" ,
"v" ,	"श्" ,
"w" ,	"ष्" ,
"x" ,	"स्" ,
"y" ,	"ह्" ,
"z" ,	"श्" ,
"U" ,	"र" ,
"V" ,	"ळ" ,
"W" ,	"ह" ,
"||" ,	"॥" ,
"|" ,	"।" ,
"Å" ,	"ऽ" ,
"Æ" ,	"ँ" ,
"ð" ,	"ँ" ,
"Ç" ,	"ं" ,
"È" ,	"ः" ,
//"¡" ,	"ः" ,
"É" ,	"ा" ,
"Ê" ,	"ा" ,
"Ï" ,	"ी" ,
"Ð" ,	"ी" ,
"Ñ" ,	"ु" ,
"Ò" ,	"ु" ,
"Ó" ,	"ु" ,
"Ô" ,	"ू" ,
"Õ" ,	"ू" ,
"Ö" ,	"ू" ,
"×" ,	"ृ" ,
"Ø" ,	"ृ" ,
"Ù" ,	"ृ" ,
"Ú" ,	"ॄ" ,
"Û" ,	"ॄ" ,
"Ü" ,	"ॄ" ,
"ã" ,	"ॆ" ,
"ä" ,	"ॅ" ,
"å" ,	"े" ,
"æ" ,	"ै" ,
"ç" ,	"्" ,
"è" ,	"्" ,
"é" ,	"्" ,
"`" ,	"‘" ,
"्ा" ,	"" ,
"्ो" ,	"े" ,
"्ौ" ,	"ै" ,
"अो" ,	"ओ" ,
"अा" ,	"आ" ,
"आै" ,	"औ" ,
"आे" ,	"ओ" ,
"ाो" ,	"ो" ,
"ाॅ" ,	"ॉ" ,
"ॅा" ,	"ॉ" ,
"ाे" ,	"ो" ,
"ंु" ,	"ुं" ,
"ेे" ,	"े" ,
"अै" ,	"अ‍ै" ,
"ाे" ,	"ो" ,
"अे" ,	"अ‍े" ,
"ंा" ,	"ां" ,
"अॅ" ,	"अ‍ॅ" ,
"ाै" ,	"ौ" ,
"ैा" ,	"ौ" ,
"ंृ" ,	"ृं" ,
"ँा" ,	"ाँ" ,
"ँू" ,	"ूँ" ,
"ेा" ,	"ो" ,
"ंे" ,	"ें" ,
"ाें" ,	"ों" ,
"ॅं" ,	"ँ" ,
"ंॅ" ,	"ँ" ,
" ः" ,	" :" ,
"ंू" ,	"ूं"  ,

"0" ,"०" ,
"1" ,"१" ,
"2" ,"२" ,
"3" ,"३" ,
"4" ,"४" ,
"5" ,"५" ,
"6" ,"६" ,
"7" ,"७" ,
"8" ,"८" ,
"9" ,"९" ,

"गःे" , "गे" ,   
"गःं" , "गं" ,
"य्ँ" , "यँ्"		)     

// Remove typing mistakes in the original file 

    var array_one_length = array_one.length ;

    var modified_substring = document.getElementById("barah_text").value  ;

    Replace_Symbols( ) ;

    processed_text = modified_substring ;

    document.getElementById("legacy_text").value = processed_text  ;

// --------------------------------------------------


function Replace_Symbols( )

{

if ( modified_substring != "" )  // if stringto be converted is non-blank then no need of any processing.

{
// is dot of nga
modified_substring = modified_substring.replace( /([ÆðÇÑÒÓÔÕÔÕÖ×ØÙÚÛÜãäåæç]*)¡/g , "¡$1" ) ;

// remove space after choti i
modified_substring = modified_substring.replace( /([ËÌÍÎ])([\s]+)/g , "$1" ) ;

//remove spaces before matraas
modified_substring = modified_substring.replace( /\s([ÅÆðÇÈ¡ÉÊÏÐÑÒÓÔÕÔÕÖ×ØÙÚÛÜãäåæç])/g , "$1" ) ;

//substitute the corresponding pair from array_one

for ( input_symbol_idx = 0;   input_symbol_idx < array_one_length-1;    input_symbol_idx = input_symbol_idx + 2 )

{ 

idx = 0  ;  // index of the symbol being searched for replacement

while (idx != -1 ) //while-00
{

modified_substring = modified_substring.replace( array_one[ input_symbol_idx ] , array_one[input_symbol_idx+1] )
idx = modified_substring.indexOf( array_one[input_symbol_idx] )

} // end of while-00 loop

} // end of for loop

//******************************

//"Ë","Ì","Í","Î",

modified_substring = modified_substring.replace( /[ÌÍÎ]/g , "Ë" ) ;

var position_of_i = modified_substring.indexOf( "Ë" )

while ( position_of_i != -1 )  //while-02
{
var charecter_next_to_i = modified_substring.charAt( position_of_i + 1 )
var charecter_to_be_replaced = "Ë" + charecter_next_to_i
modified_substring = modified_substring.replace( charecter_to_be_replaced , charecter_next_to_i + "ि" ) 
position_of_i = modified_substring.search( /Ë/ , position_of_i + 1 ) // search for i ahead of the current position.

} // end of while-02 loop

//**********************************************************************************
// End of Code for Replacing four Special glyphs
//**********************************************************************************

// following loop to eliminate 'chhotee ee kee maatraa' on half-letters as a result of above transformation.

var position_of_wrong_ee = modified_substring.indexOf( "ि्" ) 

while ( position_of_wrong_ee != -1 )  //while-03

{
var consonent_next_to_wrong_ee = modified_substring.charAt( position_of_wrong_ee + 2 )
var charecter_to_be_replaced = "ि्" + consonent_next_to_wrong_ee 
modified_substring = modified_substring.replace( charecter_to_be_replaced , "्" + consonent_next_to_wrong_ee + "ि" ) 
position_of_wrong_ee = modified_substring.search( /ि्/ , position_of_wrong_ee + 2 ) // search for 'wrong ee' ahead of the current position. 

} // end of while-03 loop

// following loop to eliminate 'chhotee ee kee maatraa' on half-letters as a result of above transformation.

var position_of_wrong_ee = modified_substring.indexOf( "िं्" ) 

while ( position_of_wrong_ee != -1 )  //while-03

{
var consonent_next_to_wrong_ee = modified_substring.charAt( position_of_wrong_ee + 3 )
var charecter_to_be_replaced = "िं्" + consonent_next_to_wrong_ee 
modified_substring = modified_substring.replace( charecter_to_be_replaced , "्" + consonent_next_to_wrong_ee + "िं" ) 
position_of_wrong_ee = modified_substring.search( /िं्/ , position_of_wrong_ee + 3 ) // search for 'wrong ee' ahead of the current position. 

} // end of while-03 loop

//========================

// Eliminating reph "ï" and putting 'half - r' at proper position for this.

modified_substring = modified_substring.replace ( /इïं/g , "ईं" ) ;
modified_substring = modified_substring.replace ( /इï/g , "ई" ) ;

modified_substring = modified_substring.replace( /([कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ])([ा\ि\ी\ु\ू\ृ\े\ै\ो\ौ\ं\ँ]*)([ï])/g , "$3$1$2" ) ;

modified_substring = modified_substring.replace( /(([कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ]्)+)([ï])/g , "$3$1" ) ;

// here, Z is $3 and NOT $2.

modified_substring = modified_substring.replace( /ï/g , "र्" ) ;

//=========================

// space + maatraa --> maatraa
modified_substring = modified_substring.replace
( /([ ]+)([ऽ\्\ा\ी\ु\ू\ृ\े\ै\ो\ौ\ं\ँ\ः])/g , "$2" ) ;

// remove maatras typed wrongly , especially double maatras

modified_substring = modified_substring.replace( /([ंँ])([ा\ि\ी\ु\ू\ृ\े\ै\ो\ौ])/g , "$2$1" );

modified_substring = modified_substring.replace( /([ा\ि\ी\ु\ू\ृ\े\ै\ो\ौ\ं\ँ])([ा\ि\ी\ु\ू\ृ\े\ै\ो\ौ])/g , "$1" ) ;

} // end of IF  statement  meant to  supress processing of  blank  string.

} // end of the function  Replace_Symbols

} // end of convert_to_unicode function
