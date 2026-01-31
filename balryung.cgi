
sub BALRYUNG{
						$ksub2=0;
						$uhit=0;
						foreach(@UNI_DATA){
							($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
							if("$uid" eq "$kid" && $unit_id eq $kid){$uhit=1;last;}
						}
						if(!$uhit){
							&K_LOG("$mmonth월 : 대장밖에 실행할 수 없습니다.");
						}else{

							foreach(@UNI_DATA){
								($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
								if($unit_id eq $kid && $uid ne $unit_id){
									open(IN,"./charalog/main/$uid\.cgi");
									@E_DATA = <IN>;
									close(IN);
									($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
									if($csub eq $ename){							
									$epos = $cnum;
									&E_LOG2("$mmonth월 : 대장의 명령에 의해 $town_name[$cnum]성으로 발령되었습니다.");
									&ENEMY_INPUT;
									}
								}
							}
							$kcha_ex++;
							$go_ex += int($kbank/5);
							$kcex+=30;
							$kpoint += 10;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
							&K_LOG("$mmonth월 : $csub님을 $town_name[$cnum]성으로 발령보냈습니다.");
						}
}
1;

