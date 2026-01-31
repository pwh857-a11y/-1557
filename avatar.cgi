#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

&DECODE;
&BODY;

sub BODY {



	if ($in{'id'} =~ /[^0-9a-zA-Z]/){
		&ERR2("에러입니다.");
	}

	&TOWN_DATA_OPEN("$kpos");

	open(IN,"./charalog/main/$in{'id'}.cgi") or &ERR2('ID와 패스가 올바르지 않습니다!');
	@CN_DATA = <IN>;
	close(IN);

	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/,$CN_DATA[0]);
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex) = split(/,/,$ksub1);

	&CHARA_ITEM_OPEN;


	print "Cache-Control: no-cache\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html\n\n";

print <<"EOM";
<title>칠랑서버 $kname 열전</title>
<html>
<body bgcolor="white" text="black" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" background="$IMG/avatarb.gif">
            <div id="pro" style="width:34px; height:44px; position:absolute; left:0px; top:0px; z-index:1;">
    <p><img src="$IMG/pro[$kbook].gif" width="34" height="44" border="0"></p>
            </div>
            <div id="arm" style="width:34px; height:44px; position:absolute; left:0px; top:0px; z-index:1;">
    <p><img src="$IMG/arm[$karm].gif" width="34" height="44" border="0"></p>
            </div></body>
</html>
EOM

}
