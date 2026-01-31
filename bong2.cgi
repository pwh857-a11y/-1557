#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("로딩중입니다. 잠시만 기다려 주십시오."); }
&DECODE;
&BONG2;


sub BONG2 {

	&CHARA_MAIN_OPEN;
	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($in{'num'});
	&COUNTRY_DATA_OPEN($kcon);


	if($in{'jangsu'} eq ""){&ERR("장수가 선택되지 않았습니다.");}
	if($in{'num'} eq ""){&ERR("도시가 선택되지 않았습니다.");}
	if($in{'bongto'} eq ""){&ERR("하사할 봉토를 선택하지 않았습니다.");}

	open(IN,"$TOWN_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@TOWN_DATA = <IN>;
	close(IN);

	$num1=0;
	foreach(@TOWN_DATA){
	($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/);
	if($in{'jangsu'} eq $zbong1 || $in{'jangsu'} eq $zbong2 || $in{'jangsu'} eq $zbong3){
	&ERR("이미 다른 곳에 봉토를 소유하고 있는 장수입니다.");
	}
	}
	foreach(@TOWN_DATA){
	($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/);
	if($in{'num'} eq $num1){
	if($in{'bongto'} eq "1"){
		$zbong1 = "$in{'jangsu'}";
	}elsif($in{'bongto'} eq "2"){
		$zbong2 = "$in{'jangsu'}";
	}elsif($in{'bongto'} eq "3"){
		$zbong3 = "$in{'jangsu'}";
	}
		&TOWN_DATA_INPUT; 
	}
	$num1++;
	}

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/);
		if("$in{'jangsu'}" eq "$eid"){
			$jangsu = "$ename";

	open(IN,"./charalog/per/$eid.cgi");
	@KK = <IN>;
	close(IN);


	open(OUT,">./charalog/per/$eid.cgi");
	print OUT @KK;
	close(OUT);
		}
	}


	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$jangsu님에게 $town_name[$in{'num'}]성의 봉토를 하사했습니다.</h2><p>
<form action="./bong.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=BONG>
<input type=hidden name=num value=$in{'num'}>
<input type=submit value="확인"></form></CENTER>

EOM

	&FOOTER;
	exit;

}
