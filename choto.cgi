
sub CHOTO{
						$ksub2=0;
						&COUNTRY_DATA_OPEN("$kcon");
						if($kgold<500){
							&K_LOG("$mmonth월 : 자금부족으로 실행할 수 없었습니다.");
						}elsif($xking eq "$kid" || $x0 eq "$kid"){
						&TOWN_DATA_OPEN("$kpos");
						$znou = 0;
						$zsyo = 0;
						$znum = 0;
						$zsub1 = 0;
						$zpri = 0;
						$zdef_att = 0;
						$$zshiro = 0;
						$kgold-=500;
						$kclass = $kclass * 0.8;
						if("$zname" ne ""){
							splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
						}

						&MAP_LOG("<img src=$IMG/b19.gif> $zname성이 초토화되어 불타고 있습니다.");
						&K_LOG("$mmonth월 : 도시가 초토화되어 불타고 있습니다.");
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}else{
							&K_LOG("$mmonth월 : 군주만이 이 커맨드를 실행할 수 있습니다.");
						}
}
1;

