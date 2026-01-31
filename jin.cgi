#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("로딩중입니다. 잠시만 기다려 주십시오"); }
&DECODE;

&INDEX;

sub INDEX {

	if ($in{'id'} =~ /[^0-9a-zA-Z]/){
		&ERR2("에러입니다.");
	}



	open(IN,"./charalog/main/$in{'id'}.cgi") or &ERR2('ID와 패스가 올바르지 않습니다!');
	@CN_DATA = <IN>;
	close(IN);

	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct) = split(/<>/,$CN_DATA[0]);
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex) = split(/,/,$ksub1);

	print <<"EOM";
	<form action="jin.cgi" method="post" name=para><input type="hidden" name="mode" value="JIN">
	<input type="radio" name="jin" value="1">진법1<br>
	<input type="radio" name="jin" value="2">진법2<br>
	<input type="radio" name="jin" value="3">진법3<br>
	<input type="radio" name="jin" value="4">진법4<br>
	<input type="radio" name="jin" value="5">진법5<br>
	<input type="submit" style="font-family:궁서; color:rgb(255,153,0); background-color:rgb(41,60,66); border-style:none;" value="진법설정"></form>
EOM

	&FOOTER;
	exit;
}

sub JIN {
	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct) = split(/<>/,$page[0]);
			$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$kjin,";
			$kjin = $in{'jin'};
			&CHARA_MAIN_INPUT;
			}}
	closedir(dirlist);

	if($in{'jin'} eq 1){
	$jinb = '진법1';
	}elsif($in{'jin'} eq 2){
	$jinb = '진법2';
	}elsif($in{'jin'} eq 3){
	$jinb = '진법3';
	}elsif($in{'jin'} eq 4){
	$jinb = '진법4';
	}elsif($in{'jin'} eq 5){
	$jinb = '진법5';
	}

	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$jinb로 진법을 설정하였습니다.</font></h2><hr size=0>
<br>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form>
EOM

	&FOOTER;
	exit;
}