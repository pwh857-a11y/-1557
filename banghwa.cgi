
sub BANGHWA{
				$ksub2=0;
				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3) = split(/<>/,$TOWN_DATA[$cnum]);
				if($zcon eq $kcon){
					&K_LOG("$mmonth월 : 자국에는 방화를 할 수 없습니다.");
				}elsif($z[0] ne $kpos && $z[1] ne $kpos && $z[2] ne $kpos && $z[3] ne $kpos && $z[4] ne $kpos && $z[5] ne $kpos && $z[6] ne $kpos && $z[7] ne $kpos ){
					&K_LOG("$mmonth월 : $zname성에 인접하고 있지 않습니다.");
				}elsif($kgold<100){
					&K_LOG("$mmonth월 : 자금부족으로 실행할 수 없었습니다.");
				}else{
					$kgold -= 100;
					($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3) = split(/<>/,$TOWN_DATA[$cnum]);
					$d_hit=0;
					foreach(@DEF_DATA){
						($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex) = split(/<>/);
						if($cnum eq $dtown_id){
							$d_hit++;
						}
					}
					$rate = int(rand(int($kintt)+rand(120)-$d_hit*20));
					$rate2 = int(rand(2))*int(rand(2))*int(rand(2))*int(rand(2))*int(rand(2))*int(rand(2));
					if($zcon eq ""){
						&K_LOG("$mmonth월 : 공백지가지고 장난치지 맙시다^^; [벌칙:피로도 100 증가, 금 1000 감소]");
						$kgold -= 900;
						$go_ex += 100;
					}elsif($rate<80 && $rate2==0){
						&K_LOG("$mmonth월 : 공작원이 잡혀버려 $zname성의 방화는 실패했습니다.");
						&MAP_LOG("<img src=$IMG/j18.gif> $kname에 의해 $zname성의 방화는 실패했습니다.");
					}else{
						if($rate<80){
							&MAP_LOG("<img src=$IMG/j18.gif> $kname에 의해 $zname성의 방화는 <font color=red>성공</font>되었습니다.");
						}else{
							&MAP_LOG("<img src=$IMG/j18.gif> 누군가에 의해 $zname성의 방화는 <font color=red>성공</font>되었습니다.");
						}
						$znou_dmg = int(rand($znou*0.1)+$znou*0.05);
						$zsyo_dmg = int(rand($zsyo*0.1)+$zsyo*0.05);
						$zsub1_dmg = int(rand($zsub1*0.1)+$zsub1*0.05);

						$znou -= $znou_dmg;
						$zsyo -= $zsyo_dmg;
						$zsub1 -= $zsub1_dmg;

						if($znou < 0){
							$znou = 0;
						}
						if($zsyo < 0){
							$zsyo = 0;
						}
						if($zsub1 < 0){
							$zsub1 = 0;
						}
					
						if("$zname" ne ""){
							splice(@TOWN_DATA,$cnum,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
						}

						&K_LOG("$mmonth월 : $zname성의 방화로 인해 농업치 <font color=red>-$znou_dmg</font>, 상업치 <font color=red>-$zsyo_dmg</font>, 기술력 <font color=red>-$zsub1_dmg</font>로 각각 하락되었습니다.");
						$kcex += 50;
						$kexp += 50;
						$kpoint += 15;
						$kstr_ex += 3;
					}
					$go_ex += int($kbank/5);
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
				}
}
1;

