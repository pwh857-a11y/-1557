sub BATTLE2 {
	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	if($in{'num'} eq ""){&ERR("쳐들어가는 곳을 입력하지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	$num = $in{'num'};
	$hit=0;

	$hoya = int($SOL_RICE[$ksub1_ex]*($ksol/60));

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"18<><>$town_name[$num]에 출병 (소모군량:$hoya)<>$tt<><>$in{'num'}<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);

			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"18<><>$town_name[$num]에 출병 (소모군량:$hoya)<>$tt<><>$in{'num'}<><>\n");
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
<CENTER><hr size=0><h2>NO:$no에 $town_name[$num]에 출병을 입력했습니다. (소모군량:$hoya)</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인 "></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;