
sub YUWON{
				$ksub2=0;
				($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$zz[0],$zz[1],$zz[2],$zz[3],$zz[4],$zz[5],$zz[6],$zz[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/,$TOWN_DATA[$cnum]);
				if($zzcon eq $kcon){
					&K_LOG("$mmonth월 : 자국에 유언비어를 퍼뜨릴 수가 없습니다.");
				}elsif($zz[0] ne $kpos && $zz[1] ne $kpos && $zz[2] ne $kpos && $zz[3] ne $kpos && $zz[4] ne $kpos && $zz[5] ne $kpos && $zz[6] ne $kpos && $zz[7] ne $kpos ){
					&K_LOG("$mmonth월 : $zname성에 인접하지 않고 있습니다.");
				}elsif($kgold<100){
					&K_LOG("$mmonth월 : 자금부족으로 실행할 수 없었습니다.");
				}else{
					$kgold -= 100;
					($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3) = split(/<>/,$TOWN_DATA[$cnum]);
					$rate = int(rand(int($kcha+$kcha2)+110-$zpri));
					$rate2 = int(rand(2))*int(rand(2))*int(rand(2))*int(rand(2))*int(rand(2))*int(rand(2));
					if($zcon eq ""){
						&K_LOG("$mmonth월 : 편법으로 매력올리시느라 수고가 많으십니다. [벌칙:피로도 100 증가, 금 2000 감소]");
						$kgold -= 1900;
						$go_ex += 100;
					}elsif( $rate < 50 && $rate2 == 0 ){
						&K_LOG("$mmonth월 : 공작원이 잡혀버려 $zname성에 유언비어를 퍼뜨릴 수 없었습니다.");
						&MAP_LOG("<img src=$IMG/j18.gif> $kname에 의해 $zname성의 유언비어는 실패로 돌아갔습니다.");
					}else{
						if($rate < 50){
							&MAP_LOG("<img src=$IMG/j18.gif> $kname에 의해 $zname성의 유언비어는 <font color=blue>성공</font>되었습니다.");
						}else{
							&MAP_LOG("<img src=$IMG/j18.gif> 누군가에 의해 $zname성의 유언비어는 <font color=red>성공</font>되었습니다.");
						}
						$zpri_dmg = int(rand($zpri*0.15)+$zpri*0.05);
						$zpri -= $zpri_dmg;
						if($zpri < 0){
						$zpri = 0;
						}
						if("$zname" ne ""){
							splice(@TOWN_DATA,$cnum,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
						}

						&K_LOG("$mmonth월 : $zname성에서 유언비어가 흉흉하게 나돌아 민심이 <font color=red>-$zpri_dmg</font>로 하락되었습니다.");
						$kcex += 50;
						$kexp += 50;
						$kpoint += 15;
						$kcha_ex += 3;
					}
					$go_ex += int($kbank/5);
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
				}
}
1;

