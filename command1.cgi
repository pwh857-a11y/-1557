#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("로딩중입니다. 잠시만 기다려 주십시오."); }
&DECODE;
&COM1;


sub COM1 {


	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TIME_DATA;

	open(IN,"./charalog/command1/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > 30) { pop(@COM_DATA); }


	if($in{'mode'} eq 0){
		$comname = "일반공격";
		$cpoint = 0;
		$cra = 0;
	}elsif($in{'mode'} eq 1){
		$comname = "추행진";
		$cpoint = 25;
		$cra = 1;
	}elsif($in{'mode'} eq 2){
		$comname = "원진";
		$cpoint = 25;
		$cra = 2;
	}elsif($in{'mode'} eq 3){
		$comname = "장사진";
		$cpoint = 25;
		$cra = 3;
	}elsif($in{'mode'} eq 4){
		$comname = "어린진";
		$cpoint = 75;
		$cra = 1;
	}elsif($in{'mode'} eq 5){
		$comname = "방원진";
		$cpoint = 75;
		$cra = 2;
	}elsif($in{'mode'} eq 6){
		$comname = "안행진";
		$cpoint = 75;
		$cra = 3;
	}elsif($in{'mode'} eq 11){
		$comname = "열화지옥";
		$cpoint = 150;
		$cra = 1;
	}elsif($in{'mode'} eq 12){
		$comname = "비천신무";
		$cpoint = 150;
		$cra = 2;
	}elsif($in{'mode'} eq 13){
		$comname = "구천탄망";
		$cpoint = 150;
		$cra = 3;
	}elsif($in{'mode'} eq 14){
		$comname = "신출귀몰";
		$cpoint = 100;
		$cra = 1;
	}elsif($in{'mode'} eq 15){
		$comname = "신라검법";
		$cpoint = 120;
		$cra = 3;
	}elsif($in{'mode'} eq 16){
		$comname = "원군";
		$cpoint = 300;
		$cra = 2;
	}elsif($in{'mode'} eq 17){
		$comname = "투석";
		$cpoint = 100;
		$cra = 0;
	}elsif($in{'mode'} eq 18){
		$comname = "진열화지옥";
		$cpoint = 350;
		$cra = 1;
	}

	if($kskill =~ /Gb/){
	$ctotal = int((500+($kclass/50)) * 1.2);
	}else{
	$ctotal = 500+int($kclass/50);
	}


	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < 30){
			push(@NEW_COM_DATA,"$comname<>$in{'mode'}<>$cpoint<>$cra<>\n");
			if($i eq $_){
			}else{
			$cpoin1 += $cpoint;
			}
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cname,$cno,$cp,$crap) = split(/<>/);
			$ahit=0;

			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$comname<>$in{'mode'}<>$cpoint<>$cra<>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
					$cpoin1 += $cpoint;
				}	
			}

			if(!$ahit){
					$cpoin1 += $cp;
					push(@NEW_COM_DATA,"$_");
			}

			$i++;
		}
	}

		
	if($cpoin1 > $ctotal){
	&ERR("명령포인트가 모자랍니다.");
	}

	open(OUT,">./charalog/command1/$kid.cgi") or &ERR('파일을 열지 않았습니다.');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";

<CENTER><hr size=0><h2>전투커맨드 $no턴에 $comname을 입력하였습니다. CP: $cpoin1/$ctotal</h2><p>
<form action="setting.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=TOP>
<script language="javascript">
setTimeout(form.submit(), 1);
</script>
<input type=submit value="확인"></form>


</CENTER>
EOM

	&FOOTER;

	exit;

}