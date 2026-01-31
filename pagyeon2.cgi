
sub PAGYEON2{
				$ksub2=0;
				$zhit=0;
				($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$zz[0],$zz[1],$zz[2],$zz[3],$zz[4],$zz[5],$zz[6],$zz[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3) = split(/<>/,$TOWN_DATA[$cnum]);
				
	if($zzname eq "성도" || $zzname eq "장안" || $zzname eq "양양" || $zzname eq "낙양" || $zzname eq "업" || $zzname eq "허창" || $zzname eq "건업" || $zzname eq "한"){
				$znum_limit = 100000;
	}elsif($zzname eq "홍농" || $zzname eq "완" || $zzname eq "강릉" || $zzname eq "여남" || $zzname eq "복양" || $zzname eq "수춘" || $zzname eq "계" || $zzname eq "남피" || $zzname eq "북해" || $zzname eq "하비" || $zzname eq "광릉" || $zzname eq "오" || $zzname eq "국내"){
				$znum_limit = 80000;
	}elsif($zzname eq "서량" || $zzname eq "한중" || $zzname eq "강주" || $zzname eq "강하" || $zzname eq "장사" || $zzname eq "남해" || $zzname eq "진유" || $zzname eq "시상" || $zzname eq "초" || $zzname eq "단양" || $zzname eq "북평" || $zzname eq "회계" || $zzname eq "서라벌" || $zzname eq "사비" || $zzname eq "졸본"){
				$znum_limit = 65000;
	}else{
				$znum_limit = 50000;
	}


				if($zzcon == $kcon &&($zz[0] eq $kpos || $zz[1] eq $kpos || $zz[2] eq $kpos || $zz[3] eq $kpos || $zz[4] eq $kpos || $zz[5] eq $kpos || $zz[6] eq $kpos || $zz[7] eq $kpos)){
					($gold,$rice) = split(/,/,$csub);
					if( $znum < $rice ){ $rice = $znum; }
					elsif($kleat<int($rice/100)){
					&K_LOG("$mmonth월 : 보낼 주민이 너무 많습니다.");
					}elsif($kgold<int($rice/20)){
					&K_LOG("$mmonth월 : 돈이 부족합니다.");
					}elsif($rice > int($znum_limit-$zznum)){
					&K_LOG("$mmonth월 : $town_name[$cnum]성의 주민들이 너무 많습니다. [현재위치] : $zname성");
					}else{
					$znum -= $rice;
					&TOWN_CHANGE($kpos);
					$kpos = $cnum;

					($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3) = split(/<>/,$TOWN_DATA[$kpos]);


					$znum += $rice;
					&TOWN_CHANGE($cnum);
					&K_LOG("$mmonth월 : $town_name[$cnum]성으로 주민들을 $rice명을 이주시켰습니다.");
					&MAP_LOG("<img src=$IMG/j28.gif> $kname님이 $town_name[$cnum]성으로 주민들을 이주시켰습니다.");
					$kcex += int($rice/200);
					$kexp += 30;
					$kgold -= int($rice/20);
					$kpoint += int($rice/1000);
					$klea_ex++;
					$go_ex += int($kbank/5);
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}
					}else{
					&K_LOG("$mmonth월 : $town_name[$cnum]성으로 이주할 수가 없습니다. [현재위치] : $zname성");
				}

}
1;

