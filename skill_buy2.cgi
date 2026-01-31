sub SKILL_BUY2 {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	if($in{'select'} eq ""){&ERR("특기가 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	open(IN,"$SKILL_LIST") or &ERR('파일을 열지 않았습니다.');
	@SKILL_DATA = <IN>;
	close(IN);

	$num = $in{'select'};
	($dk,$eskillcode,$eskillpoint) = split(/<>/,$SKILL_DATA[$num]);

	$hit=0;

	if($eskillcode =~ /Ab/ && $kskill !~ /Aa/){&ERR("특기 거래을 배우기 위해서는 먼저 농업을 배우셔야 합니다.");}
	if($eskillcode =~ /Ac/ && $kskill !~ /Ab/){&ERR("특기 덕망을 배우기 위해서는 먼저 거래을 배우셔야 합니다.");}
	if($eskillcode =~ /Bb/ && $kskill !~ /Ba/){&ERR("특기 수완을 배우기 위해서는 먼저 상업을 배우셔야 합니다.");}
	if($eskillcode =~ /Bc/ && $kskill !~ /Bb/){&ERR("특기 고용을 배우기 위해서는 먼저 수완을 배우셔야 합니다.");}
	if($eskillcode =~ /Cb/ && $kskill !~ /Ca/){&ERR("특기 회피를 배우기 위해서는 먼저 기술을 배우셔야 합니다.");}
	if($eskillcode =~ /Cc/ && $kskill !~ /Ca/){&ERR("특기 연구를 배우기 위해서는 먼저 회피를 배우셔야 합니다.");}
	if($eskillcode =~ /Db/ && $kskill !~ /Da/){&ERR("특기 모병을 배우기 위해서는 먼저 양성을 배우셔야 합니다.");}
	if($eskillcode =~ /Dc/ && $kskill !~ /Db/){&ERR("특기 설치를 배우기 위해서는 먼저 모병을 배우셔야 합니다.");}
	if($eskillcode =~ /Eb/ && $kskill !~ /Ea/){&ERR("특기 독려를 배우기 위해서는 먼저 훈련을 배우셔야 합니다.");}
	if($eskillcode =~ /Ec/ && $kskill !~ /Eb/){&ERR("특기 원전을 배우기 위해서는 먼저 독려를 배우셔야 합니다.");}
	if($eskillcode =~ /Fb/ && $kskill !~ /Fa/){&ERR("특기 매료를 배우기 위해서는 먼저 민심을 배우셔야 합니다.");}
	if($eskillcode =~ /Fc/ && $kskill !~ /Fb/){&ERR("특기 매전을 배우기 위해서는 먼저 매료를 배우셔야 합니다.");}
	if($eskillcode =~ /Gb/ && $kskill !~ /Ga/){&ERR("특기 병략를 배우기 위해서는 먼저 고양을 배우셔야 합니다.");}
	if($eskillcode =~ /Gc/ && $kskill !~ /Gb/){&ERR("특기 일섬을 배우기 위해서는 먼저 병략을 배우셔야 합니다.");}

	if($eskillcode =~ /Aa/ && $kskill =~ /Aa/){&ERR("이미 농업을 배우셨습니다.");}
	if($eskillcode =~ /Ab/ && $kskill =~ /Ab/){&ERR("이미 거래를 배우셨습니다.");}
	if($eskillcode =~ /Ac/ && $kskill =~ /Ac/){&ERR("이미 덕망을 배우셨습니다.");}
	if($eskillcode =~ /Ba/ && $kskill =~ /Ba/){&ERR("이미 상업을 배우셨습니다.");}
	if($eskillcode =~ /Bb/ && $kskill =~ /Bb/){&ERR("이미 수완을 배우셨습니다.");}
	if($eskillcode =~ /Bc/ && $kskill =~ /Bc/){&ERR("이미 고용을 배우셨습니다.");}
	if($eskillcode =~ /Ca/ && $kskill =~ /Ca/){&ERR("이미 기술을 배우셨습니다.");}
	if($eskillcode =~ /Cb/ && $kskill =~ /Cb/){&ERR("이미 회피를 배우셨습니다.");}
	if($eskillcode =~ /Cc/ && $kskill =~ /Cc/){&ERR("이미 연구를 배우셨습니다.");}
	if($eskillcode =~ /Da/ && $kskill =~ /Da/){&ERR("이미 양성을 배우셨습니다.");}
	if($eskillcode =~ /Db/ && $kskill =~ /Db/){&ERR("이미 모병을 배우셨습니다.");}
	if($eskillcode =~ /Dc/ && $kskill =~ /Dc/){&ERR("이미 설치를 배우셨습니다.");}
	if($eskillcode =~ /Ea/ && $kskill =~ /Ea/){&ERR("이미 훈련을 배우셨습니다.");}
	if($eskillcode =~ /Eb/ && $kskill =~ /Eb/){&ERR("이미 독려를 배우셨습니다.");}
	if($eskillcode =~ /Ec/ && $kskill =~ /Ec/){&ERR("이미 원전을 배우셨습니다.");}
	if($eskillcode =~ /Fa/ && $kskill =~ /Fa/){&ERR("이미 민심을 배우셨습니다.");}
	if($eskillcode =~ /Fb/ && $kskill =~ /Fb/){&ERR("이미 매료를 배우셨습니다.");}
	if($eskillcode =~ /Fc/ && $kskill =~ /Fc/){&ERR("이미 매전을 배우셨습니다.");}
	if($eskillcode =~ /Ga/ && $kskill =~ /Ga/){&ERR("이미 고양을 배우셨습니다.");}
	if($eskillcode =~ /Gb/ && $kskill =~ /Gb/){&ERR("이미 병략을 배우셨습니다.");}
	if($eskillcode =~ /Gc/ && $kskill =~ /Gc/){&ERR("이미 일섬을 배우셨습니다.");}

	if($kpoint < $eskillpoint){&ERR("특기 포인트가 부족합니다.");}

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	if($in{'select'} eq 0){
	$name = '농업';
	}
	if($in{'select'} eq 1){
	$name = '거래';
	}
	if($in{'select'} eq 2){
	$name = '덕망';
	}
	if($in{'select'} eq 3){
	$name = '상업';
	}
	if($in{'select'} eq 4){
	$name = '수완';
	}
	if($in{'select'} eq 5){
	$name = '고용';
	}
	if($in{'select'} eq 6){
	$name = '기술';
	}
	if($in{'select'} eq 7){
	$name = '회피';
	}
	if($in{'select'} eq 8){
	$name = '연구';
	}
	if($in{'select'} eq 9){
	$name = '양성';
	}
	if($in{'select'} eq 10){
	$name = '모병';
	}
	if($in{'select'} eq 11){
	$name = '설치';
	}
	if($in{'select'} eq 12){
	$name = '훈련';
	}
	if($in{'select'} eq 13){
	$name = '독려';
	}
	if($in{'select'} eq 14){
	$name = '원전';
	}
	if($in{'select'} eq 15){
	$name = '민심';
	}
	if($in{'select'} eq 16){
	$name = '매료';
	}
	if($in{'select'} eq 17){
	$name = '매전';
	}
	if($in{'select'} eq 18){
	$name = '고양';
	}
	if($in{'select'} eq 19){
	$name = '병략';
	}
	if($in{'select'} eq 20){
	$name = '일섬';
	}

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;

	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"$in{'mode'}<><>특기 $name를 배운다.<>$tt<><>$num<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<><>특기 $name를 배운다<>$tt<><>$num<><>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}
			$i++;
		}
	}

	open(OUT,">./charalog/command/$kid.cgi") or &ERR('파일을 열지 않았습니다.');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>NO:$no에 특기 $name을 배움으로 입력했습니다.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;