#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("로딩중입니다. 잠시만 기다려 주십시오."); }
&DECODE;
&BAK;


sub BAK {

	&CHARA_MAIN_OPEN;


	open(IN,"./charalog/bak/$in{'id'}.cgi");
	@KK = <IN>;
	close(IN);

	unshift(@KK,"$kid<>$kpass<>$kname<>$kchara<>$kstr<>$kint<>$klea<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$kpos<>$kmes<>$khost<>$kdate<>$kmail<>$kos<>$kskill<>$kpoint<>$kct<>$klevel<>$kexp<>$kcodea<>$kcodeb<>$kqpoint<>\n");

	open(OUT,">./charalog/bak/$in{'id'}.cgi");
	print OUT @KK;
	close(OUT);


	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$in{'id'}님의 데이터를 백업했습니다.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>

EOM

	&FOOTER;
	exit;

}