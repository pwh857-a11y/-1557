
sub PAGYEON{
				$ksub2=0;
				$zhit=0;
				($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$zz[0],$zz[1],$zz[2],$zz[3],$zz[4],$zz[5],$zz[6],$zz[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3) = split(/<>/,$TOWN_DATA[$cnum]);
				
				if($zzcon == $kcon &&($zz[0] eq $kpos || $zz[1] eq $kpos || $zz[2] eq $kpos || $zz[3] eq $kpos || $zz[4] eq $kpos || $zz[5] eq $kpos || $zz[6] eq $kpos || $zz[7] eq $kpos)){
					($gold,$rice) = split(/,/,$csub);
					if( $zshiro < $rice ){ $rice = $zshiro; }
					elsif($kleat<int($rice/100)){
					&K_LOG("$mmonth월 : 보낼 원군이 너무 많습니다.");
					}elsif($kgold<int($rice/20)){
					&K_LOG("$mmonth월 : 돈이 부족합니다.");
					}elsif($rice > int($zzshiro_max-$zzshiro)){
					&K_LOG("$mmonth월 : $town_name[$cnum]성의 수비병이 많습니다. [현재위치] : $zname성");
					}else{
					$zshiro -= $rice;
					&TOWN_CHANGE($kpos);

					$kpos = $cnum;

					($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3) = split(/<>/,$TOWN_DATA[$kpos]);

					$zshiro += $rice;
					&TOWN_CHANGE($kpos);
					&K_LOG("$mmonth월 : $town_name[$cnum]성으로 수비병을 $rice명을 파견하였습니다.");
					&MAP_LOG("<img src=$IMG/j23.gif> $kname님이 $town_name[$cnum]성으로 원군을 파견하고 있습니다.");
					$kcex += int($rice/200);
					$kexp += 30;
					$kgold -= int($rice/20);
					$kpoint += int($rice/1000);
					$klea_ex++;
					$go_ex += int($kbank/5);
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}
					}else{
					&K_LOG("$mmonth월 : $town_name[$cnum]성으로 파견할 수가 없습니다. [현재위치] : $zname성");
				}

}
1;