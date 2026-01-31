
sub WAR{
						$ksub2=0;
						($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/,$TOWN_DATA[$cnum]);
						if($zcon eq $kcon){
							&K_LOG("$mmonth월 : 자국에는 공격받지 않습니다.");
						}elsif($ksol < 1){
							&K_LOG("$mmonth월 : 병력이 없습니다.");
						}elsif($z[0] ne $kpos && $z[1] ne $kpos && $z[2] ne $kpos && $z[3] ne $kpos && $z[4] ne $kpos && $z[5] ne $kpos && $z[6] ne $kpos && $z[7] ne $kpos ){
							&K_LOG("$mmonth월 : $zname에는 인접하고 있지 않습니다.");
						}else{


							open(IN,"$COUNTRY_LIST");
							@COU_DATA = <IN>;
							close(IN);
							@NEW_COU_DATA=();
							$zvhit=0;
							foreach(@COU_DATA){
								($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri)=split(/<>/);
								if($xvcid eq $zcon){$zvhit=1;last;}
							}
							if($zvhit && $xvmark < $BATTLE_STOP){
								&K_LOG("$mmonth월 : $xvname국에게는 아직 공격받지 않습니다. ($xvmark 턴)");
							}else{
								&COUNTRY_DATA_OPEN("$kcon");
								if($xmark < $BATTLE_STOP){
									&K_LOG("$mmonth월 : $xname국은 아직 공격받지 않습니다. ($xmark 턴)");
								}else{
									open(IN,"$DEF_LIST");
									@DEF_LIST3 = <IN>;
									close(IN);
									$d_hit=0;
									foreach(@DEF_LIST3){
										($mdid,$mdname,$mdtown_id,$mdtown_flg,$mdcon,$mdchara) = split(/<>/);
										if($cnum eq $mdtown_id){
											$d_hit=1;last;
										}
									}
									$katt_add2 = 0;
									$kcex += 20;
									$kexp += 20;
									$kpoint += 6;
									&MAP_LOG("<img src=$IMG/j1.gif> $xname국의 $kname부대는 $zname성으로 쳐들어 갔습니다!");

									$krice -= int($SOL_RICE[$ksub1_ex]*($ksol/60));
									$erice -= int($SOL_RICE[$esub1_ex]*($esol/60));

									$eid="";
			
					if($d_hit){
					%trap = ();
					$trapmax = @TRAP_DATA;
					for($trapi=0;$trapi<$trapmax;$trapi++){
						($tid,$tname,$ttown_id,$tcon,$ttrap,$tint) = split(/<>/,$TRAP_DATA[$trapi]);
						if( $ttown_id == $cnum ){
							$trap{$trapi} = int(rand(65535));
						}
					}

					$t_hit = 0;
					foreach(sort{$trap{$b}<=>$trap{$a}} keys %trap){
						$ttid = $_;
						$t_hit = 1;
					}
					if($t_hit){
						@trapstr = ("","화계","낙석","허보");
						($eid,$ename,$etown_id,$econ,$etrap,$eint) = split(/<>/,$TRAP_DATA[$ttid]);
						$r = int(rand($kintt));
						$ran = int(rand(2000));
						$r1 = int(rand($kleat));
						if(($r - $eint > 0 || ($ksub1_ex == 20 && $ksol > $ran)) && $ksol > 500){
							&K_LOG2("$kname님은 $ename님의 $trapstr[$etrap]를 해제했습니다.");
							&E_LOG2("$kname님에 의해 함정 $trapstr[$etrap]를 해제당했습니다.");
							splice(@TRAP_DATA,$ttid,1);
							$t_hit = 0;
						}elsif($kskill =~ /Cb/){
							&K_LOG2("$kname님은 특기 '회피'로 인해 $ename님의 $trapstr[$etrap]를 회피했습니다.");
							&E_LOG2("$kname님이 특기 '회피'로 인해 $trapstr[$etrap]를 회피해버렸습니다!");
						}elsif($ksub1_ex eq 5){
							&K_LOG2("$kname님은 군세가 신귀병이기 때문에 $ename님의 $trapstr[$etrap]를 지나쳤습니다.");
							&E_LOG2("$kname님이 군세가 신귀병이기 때문에 $trapstr[$etrap]를 지나쳤습니다!");
						}elsif($r1 - $eint > 0 || $ksub1_ex eq 5 || $kskill =~ /Cb/){
							&K_LOG2("$kname님은 군사들을 일사분란하게 지휘하여 $ename님의 $trapstr[$etrap]를 회피했습니다.");
							&E_LOG2("$kname님이 군사들을 일사분란하게 지휘하여 $trapstr[$etrap]를 회피해버렸습니다!");
						}else{
							if($etrap == 1){
								$tdm = int(($ksol/30)*$eint/15);
								if($ksol < $tdm ){
									$tdm = $ksol;
									$ksol = 0;
									$t_hit = 1;
								}else{
									$ksol -= $tdm;
									$t_hit = 0;
								}
								&K_LOG2("$ename님의 $trapstr[$etrap]가 발동! 진군중이던 $kname님의 병력 <font color=red>$tdm</font>명이 사망했습니다.");
								&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : $ename의 $trapstr[$etrap]가 발동하여 진군중이던 $kname의 병력이 피해를 입은 듯 하다!</font>");
								&E_LOG2("$ename님의 $trapstr[$etrap]가 발동! 진군중이던 $kname님의 병력 <font color=red>$tdm</font>명이 사망했습니다.");
							}elsif($etrap == 2){
								$tdm = int(($ksol/30)*$eint/6);
								if($ksol < $tdm ){
									$tdm = $ksol;
									$ksol = 0;
									$t_hit = 1;
								}else{
									$ksol -= $tdm;
									$t_hit = 0;
								}
								&K_LOG2("$mmonth월 : $ename님의 $trapstr[$etrap]이 발동! 돌이 굴러떨어져 $kname님의 병력 <font color=red>$tdm</font>명이 사망했습니다.");
								&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$ename의 $trapstr[$etrap]이 발동하여 진군중이던 $kname의 병력이 깔려죽은 듯 하다!</font>");
								&E_LOG2("$mmonth월 : $ename님의 $trapstr[$etrap]이 발동! 돌이 굴러떨어져 $kname님의 병력 <font color=red>$tdm</font>명이 사망했습니다.");
							}elsif($etrap == 3){
								$tdm = int(($kgat*$eint)/250);
								if($kgat < $tdm ){
									$kgat = 0
								}else{
									$kgat -= $tdm;
								}
								&K_LOG2("$mmonth월 : $ename님의 $trapstr[$etrap]가 발동되어 $kname님의 병력이 혼란에 빠졌습니다!");
								&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$ename의 $trapstr[$etrap]가 발동하여 진군중이던 $kname의 부대가 혼란에 빠진 듯 하다!</font>");
								&E_LOG2("$mmonth월 : $ename님의 $trapstr[$etrap]가 발동되어 $kname님의 병력이 혼란에 빠졌습니다!");
							}

							splice(@TRAP_DATA,$ttid,1);
							open(IN,"./charalog/main/$eid\.cgi");
							@E_DATA = <IN>;
							close(IN);
							($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
							($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);
							$ecex += 20;
							$eexp += 20;
							&ENEMY_INPUT;


						}
							}
									open(IN,"./charalog/main/$mdid\.cgi");
									@E_DATA = <IN>;
									close(IN);
									($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
									($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);


									$last_battle=0;
									}else{
										&K_LOG2("전령 : $kname장군님! $zname성의 수비대가 농성을 준비하고 있습니다! 성벽을 공격하겠습니다! [방시:$zdef_att]");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : $zname성의 수비대가 농성을 준비하고 있는 듯 하다! $kname의 부대는 성벽을 공격할 태세다!</font>");
										$ename = "$zname성";
										$esol = $zshiro;
										$estrt = int($zdef_att/10);
										$egat = $zpri;
										$last_battle=1;
										$esub1_ex="14";
									}

									if($kcodea =~ /C9/ && 20 > rand(100) && $earm == 16){
										$kqpoint = 1;
										&K_LOG("$mmonth월 : 전설의 신검의 파편을 입수하였다.");
									}
									if($ecodea =~ /C9/ && 20 > rand(100) && $karm == 16){
										$eqpoint = 1;
										&E_LOG("$mmonth월 : 전설의 신검의 파편을 입수하였다.");
									}

									&K_LOG2("$mmonth월 : $xname국의 $kname부대는 $zname성에 쳐들어갔습니다!");
									&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : $xname국의 $kname부대는 $zname성에 쳐들어갔습니다!</font>");
									&E_LOG2("$mmonth월 : $xname국의 $kname부대는 $zname성의 $ename부대와 전투를 벌였습니다!");

									&CHARA_ITEM_OPEN;


									if($ksub1_ex eq 11){
									$hwarang = int(rand(3));
									if($hwarang eq 0){
										$hwarang1 = $kstrt;
									}elsif($hwarang eq 1){
										$hwarang1 = $kintt;
									}elsif($hwarang eq 2){
										$hwarang1 = $kleat;
									}else{
										$hwarang1 = $kchat;
									}
									}


									if($esub1_ex eq 11){
									$ehwarang = int(rand(3));
									if($ehwarang eq 0){
										$ehwarang1 = $estrt;
									}elsif($ehwarang eq 1){
										$ehwarang1 = $eintt;
									}elsif($ehwarang eq 2){
										$ehwarang1 = $eleat;
									}else{
										$ehwarang1 = $echat;
									}
									}

									if($last_battle eq "1"){
									if($kskill =~ /Eb/){
									$SOL_ATT[0]=20;
									$SOL_ATT[1]=50;
									$SOL_ATT[2]=30;
									$SOL_ATT[3]=50;
									}else{
									$SOL_ATT[1]=30;
									$SOL_ATT[2]=10;
									$SOL_ATT[3]=30;
									}
									$SOL_ATT[5]=$kintt;
									$SOL_ATT[6]=45;
									$SOL_ATT[7]=$kchat;
									$SOL_ATT[8]=75;
									$SOL_ATT[9]=30;
									$SOL_ATT[10]=30;
									$SOL_ATT[11]=$hwarang1;
									if($kskill =~ /Cc/){
									$SOL_ATT[12]=150+$kintt;
									}else{
									$SOL_ATT[12]=150;
									}
									$SOL_ATT[13]=$kchat;
									$SOL_ATT[15]=int($kstrt/2);
									$SOL_ATT[17]=75;
									$SOL_ATT[18]=15;
									$SOL_ATT[19]=30;
									$SOL_ATT[20]=45;
									}else{
									if($kskill =~ /Eb/){
									$SOL_ATT[0]=20;
									$SOL_ATT[1]=50;
									$SOL_ATT[2]=35;
									$SOL_ATT[3]=50;
									}else{
									$SOL_ATT[1]=30;
									$SOL_ATT[2]=15;
									$SOL_ATT[3]=30;
									}
									$SOL_ATT[4]=60;
									$SOL_ATT[5]=$kintt;
									$SOL_ATT[6]=20;
									$SOL_ATT[7]=$kintt+$kchat;
									$SOL_ATT[8]=90;
									$SOL_ATT[9]=45;
									$SOL_ATT[10]=75;
									$SOL_ATT[11]=$hwarang1;
									$SOL_ATT[13]=$kchat;
									$SOL_ATT[15]=$kstrt;
									$SOL_ATT[18]=$kleat;
									$SOL_ATT[19]=60;
									$SOL_ATT[20]=30;
									}

									if($ksub1_ex == 12){
									$SOL_DEF[14] = int($zdef_att/16);
									}else{
									$SOL_DEF[14] = int($zdef_att/8);
									}

									if($eskill =~ /Eb/){
									$SOL_DEF[0]=20;
									$SOL_DEF[1]=20;
									$SOL_DEF[2]=65;
									$SOL_DEF[3]=50;
									}else{
									$SOL_DEF[2]=45;
									$SOL_DEF[3]=30;
									}
									$SOL_DEF[4]=15;
									$SOL_DEF[5]=15;
									$SOL_DEF[6]=$eleat;
									$SOL_DEF[7]=$estrt+$echat;
									$SOL_DEF[8]=90;
									$SOL_DEF[9]=45;
									$SOL_DEF[10]=60;
									$SOL_DEF[11]=$ehwarang1;
									if($eskill =~ /Fb/){
									$SOL_DEF[13]=$echat;
									}else{
									$SOL_DEF[13]=15;
									}
									$SOL_DEF[15]=15;
									$SOL_DEF[16]=$zpri;
									$SOL_DEF[19]=45;
									$SOL_DEF[20]=30;





									if($zname2 == 1){
									$jih = "평지";
									$SOL_TYPE1[0] = "100";
									$SOL_TYPE1[1] = "95";
									$SOL_TYPE1[2] = "90";
									$SOL_TYPE1[3] = "100";
									$SOL_TYPE1[4] = "130";
									$SOL_TYPE1[5] = "100";
									$SOL_TYPE1[6] = "80";
									$SOL_TYPE1[7] = "90";
									$SOL_TYPE1[8] = "120";
									$SOL_TYPE1[9] = "80";
									$SOL_TYPE1[10] = "130";
									$SOL_TYPE1[11] = "90";
									$SOL_TYPE1[12] = "100";
									$SOL_TYPE1[13] = "110";
									$SOL_TYPE1[14] = "100";
									$SOL_TYPE1[15] = "90";
									$SOL_TYPE1[16] = "100";
									$SOL_TYPE1[17] = "100";
									$SOL_TYPE1[18] = "100";
									$SOL_TYPE1[19] = "80";
									$SOL_TYPE1[20] = "100";
													$SOL_TYPE1[21] = "110";
													$SOL_TYPE1[22] = "120";
													$SOL_TYPE1[23] = "115";
													$SOL_TYPE1[24] = "130";
													$SOL_TYPE1[25] = "125";
													$SOL_TYPE1[26] = "105";
													$SOL_TYPE1[27] = "110";
													$SOL_TYPE1[28] = "140";
													$SOL_TYPE1[29] = "120";
													$SOL_TYPE1[30] = "80";
}elsif($zname2 == 2){
									$jih = "수상";
									$SOL_TYPE1[0] = "100";
									$SOL_TYPE1[1] = "100";
									$SOL_TYPE1[2] = "100";
									$SOL_TYPE1[3] = "120";
									$SOL_TYPE1[4] = "90";
									$SOL_TYPE1[5] = "110";
									$SOL_TYPE1[6] = "110";
									$SOL_TYPE1[7] = "100";
									$SOL_TYPE1[8] = "80";
									$SOL_TYPE1[9] = "80";
									$SOL_TYPE1[10] = "70";
									$SOL_TYPE1[11] = "90";
									$SOL_TYPE1[12] = "100";
									$SOL_TYPE1[13] = "100";
									$SOL_TYPE1[14] = "100";
									$SOL_TYPE1[15] = "100";
									$SOL_TYPE1[16] = "90";
									$SOL_TYPE1[17] = "100";
									$SOL_TYPE1[18] = "80";
									$SOL_TYPE1[19] = "130";
									$SOL_TYPE1[20] = "110";
																																$SOL_TYPE1[21] = "105";
																																$SOL_TYPE1[22] = "95";
																																$SOL_TYPE1[23] = "110";
																																$SOL_TYPE1[24] = "90";
																																$SOL_TYPE1[25] = "100";
																																$SOL_TYPE1[26] = "120";
																																$SOL_TYPE1[27] = "115";
																																$SOL_TYPE1[28] = "105";
																																$SOL_TYPE1[29] = "95";
																																$SOL_TYPE1[30] = "160";

									}elsif($zname2 == 3){
									$jih = "산악";
									$SOL_TYPE1[0] = "100";
									$SOL_TYPE1[1] = "115";
									$SOL_TYPE1[2] = "120";
									$SOL_TYPE1[3] = "100";
									$SOL_TYPE1[4] = "70";
									$SOL_TYPE1[5] = "90";
									$SOL_TYPE1[6] = "100";
									$SOL_TYPE1[7] = "100";
									$SOL_TYPE1[8] = "70";
									$SOL_TYPE1[9] = "130";
									$SOL_TYPE1[10] = "60";
									$SOL_TYPE1[11] = "100";
									$SOL_TYPE1[12] = "100";
									$SOL_TYPE1[13] = "80";
									$SOL_TYPE1[14] = "100";
									$SOL_TYPE1[15] = "110";
									$SOL_TYPE1[16] = "100";
									$SOL_TYPE1[17] = "100";
									$SOL_TYPE1[18] = "110";
									$SOL_TYPE1[19] = "80";
									$SOL_TYPE1[20] = "90";
																																$SOL_TYPE1[21] = "105";
																																$SOL_TYPE1[22] = "80";
																																$SOL_TYPE1[23] = "115";
																																$SOL_TYPE1[24] = "75";
																																$SOL_TYPE1[25] = "85";
																																$SOL_TYPE1[26] = "110";
																																$SOL_TYPE1[27] = "105";
																																$SOL_TYPE1[28] = "100";
																																$SOL_TYPE1[29] = "140";
																																$SOL_TYPE1[30] = "70";

									}

									if($kskill =~ /Fc/){
									$katt = ($kstrt+$kcha+$SOL_ATT[$ksub1_ex])-int($egat/2);
									}else{
									$katt = ($kstrt+$SOL_ATT[$ksub1_ex])-int($egat/2);
									}

									if($eskill =~ /Fc/){
									$eatt = ($estrt+$echa+$SOL_DEF[$esub1_ex])-int($kgat/2);
									}else{
									$eatt = ($estrt+$SOL_DEF[$esub1_ex])-int($kgat/2);
									}



									if($ksub1_ex == 17){
										if($katt*2 < $eatt){
										$katt = $eatt;
										}
									}
										






									if($ksub1_ex == 0 || $ksub1_ex == 1 || $ksub1_ex == 3 || $ksub1_ex == 9 || $ksub1_ex == 13 || $ksub1_ex == 19 || $ksub1_ex == 20 || $ksub1_ex == 21 || $ksub1_ex == 23 || $ksub1_ex == 26 || $ksub1_ex == 27 || $ksub1_ex == 28){
										$ksuk = int($bo_ex/3);
										if($ksol >= 500 && $kgat >= 50){
										$bo_ex++;
										}
									}elsif($ksub1_ex == 4 || $ksub1_ex == 8 || $ksub1_ex == 10 || $ksub1_ex == 11){
										$ksuk = int($gi_ex/3);
										if($ksol >= 500 && $kgat >= 50){
										$gi_ex++;
										}
									}elsif($ksub1_ex == 2 || $ksub1_ex == 16 || $ksub1_ex == 15 || $ksub1_ex == 6 || $ksub1_ex == 18){
										$ksuk = int($ch_ex/3);
										if($ksol >= 500 && $kgat >= 50){
										$ch_ex++;
										}
									}elsif($ksub1_ex == 5 || $ksub1_ex == 7 || $ksub1_ex == 12 || $ksub1_ex == 17){
										$ksuk = int($gu_ex/3);
										if($ksol >= 500 && $kgat >= 50){
										$gu_ex++;
										}
									}


									if($esub1_ex == 0 || $esub1_ex == 1 || $esub1_ex == 3 || $esub1_ex == 9 || $esub1_ex == 13 || $esub1_ex == 19 || $esub1_ex == 20 || $esub1_ex == 21 || $esub1_ex == 23 || $esub1_ex == 26 || $esub1_ex == 27 || $esub1_ex == 28){
										$esuk = int($ebo_ex/3);
										if($esol >= 500 && $egat >= 50){
										$ebo_ex++;
										}
									}elsif($esub1_ex == 4 || $esub1_ex == 8 || $esub1_ex == 10 || $esub1_ex == 11){
										$esuk = int($egi_ex/3);
										if($esol >= 500 && $egat >= 50){
										$egi_ex++;
										}
									}elsif($esub1_ex == 2 || $esub1_ex == 16 || $esub1_ex == 15 || $esub1_ex == 6 || $esub1_ex == 18){
										$esuk = int($ech_ex/3);
										if($esol >= 500 && $egat >= 50){
										$ech_ex++;
										}
									}elsif($esub1_ex == 5 || $esub1_ex == 7 || $esub1_ex == 12 || $esub1_ex == 17){
										$esuk = int($egu_ex/3);
										if($esol >= 500 && $egat >= 50){
										$egu_ex++;
										}
									}
									$esub1 = "$estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex,";

									if($katt < 0){$katt = 0;}
									if($katt < 0){$kgat = 0;}
									$kex_add=0;
									$eex_add=0;
									if($eatt < 0){$eatt = 0;}
									if($eatt < 0){$egat = 0;}
									$win=0;
									$skill=0;

									
									# --- v19 troop matchup + passives (added; no deletions) ---
									my $kcounter = 0;
									my $ecounter = 0;
									my $kpassive_msg = "";
									my $epassive_msg = "";
									sub __TROOP_CLASS{
										my ($t)=@_;
										# 0=inf,1=cav,2=arc,3=sie
										return 3 if($t == 5 || $t == 7 || $t == 12 || $t == 17);
										return 1 if($t == 4 || $t == 8 || $t == 10 || $t == 11 || $t == 22 || $t == 24 || $t == 25);
										return 2 if($t == 2 || $t == 6 || $t == 15 || $t == 16 || $t == 18 || $t == 23);
										return 0;
									}
									my $kcls = __TROOP_CLASS($ksub1_ex);
									my $ecls = __TROOP_CLASS($esub1_ex);
									# 기본 상성: 기>궁, 궁>보, 보>기 (±15)
									if($kcls == 1 && $ecls == 2){ $kcounter += 15; $ecounter -= 15; }
									if($kcls == 2 && $ecls == 0){ $kcounter += 15; $ecounter -= 15; }
									if($kcls == 0 && $ecls == 1){ $kcounter += 15; $ecounter -= 15; }
									# 창병(2), 창기병(25) vs 기병 추가 보너스
									if(($ksub1_ex == 2 || $ksub1_ex == 25) && $ecls == 1){ $kcounter += 10; $ecounter -= 10; }
									if(($esub1_ex == 2 || $esub1_ex == 25) && $kcls == 1){ $ecounter += 10; $kcounter -= 10; }
									# 공성/병기(발석거/투석차) 야전 약점 (?10)
									if($kcls == 3 && $ecls != 3){ $kcounter -= 10; $ecounter += 10; }
									if($ecls == 3 && $kcls != 3){ $ecounter -= 10; $kcounter += 10; }
									# 패시브: 코끼리병 공포(보병 계열 상대시 훈련도 감소 + 추가 상성)
									if($ksub1_ex == 8 && $ecls == 0){
										$kcounter += 10; $ecounter -= 10;
										$egat -= 10; if($egat < 0){$egat=0;}
										$kpassive_msg = "코끼리병 공포로 적 훈련도 -10!";
									}
									if($esub1_ex == 8 && $kcls == 0){
										$ecounter += 10; $kcounter -= 10;
										$kgat -= 10; if($kgat < 0){$kgat=0;}
										$epassive_msg = "코끼리병 공포로 적 훈련도 -10!";
									}
									# --- end v19 troop matchup + passives ---

											if($last_battle eq "0"){
										&K_LOG2("전령 : $zname성으로부터 $ename의 $SOL_TYPE[$esub1_ex]부대가 요격을 해왔습니다!");
										&K_LOG2("$cou_name[$econ]군진영 : <$ename> <무력 $estrt> <병종 $SOL_TYPE[$esub1_ex]> <훈련 $egat> <병력 $esol> <지형 $jih> <해당병과숙련:Lv.$esuk>");
										&K_LOG2("전투력분석 : 「아군전투력 $katt 지형상성 $SOL_TYPE1[$ksub1_ex]\%」 VS 「적군전투력 $eatt 지형상성 $SOL_TYPE1[$esub1_ex]\%」");
										&E_LOG2("전령 : $kname의 $SOL_TYPE[$ksub1_ex]부대가 $zname성 앞으로 진군해왔습니다! 요격을 준비하겠습니다!");
										&E_LOG2("$cou_name[$econ]군진영 : <$kname> <무력 $kstrt> <병종 $SOL_TYPE[$ksub1_ex]> <훈련 $kgat> <병력 $ksol> <지형 $jih> <해당병과숙련:Lv.$ksuk>");
										&E_LOG2("전투력분석 : 「아군전투력 $eatt 지형상성 $SOL_TYPE1[$esub1_ex]\%」 VS 「적군전투력 $katt 지형상성 $SOL_TYPE1[$ksub1_ex]\%」");
										&BATTLE_LOG("<table border=1 width=274 align=center><tr><td width=100 bgcolor=$ELE_C[$cou_ele[$kcon]]><p align=center><img src=$IMG/$kchara\.gif></p></td><td width=52 height=171 rowspan=3 bgcolor=black><p align=center><b><font color=white>VS</font></b></p></td><td width=100 bgcolor=$ELE_C[$cou_ele[$econ]]><p align=center><img src=$IMG/$echara\.gif></p></td></tr><tr><td width=100 height=19 bgcolor=$ELE_C[$cou_ele[$kcon]]><p align=center><b>$kname<br></b></td><td width=100 height=19 bgcolor=$ELE_C[$cou_ele[$econ]]><p align=center><b>$ename</b></td></tr><tr><td width=100 height=102 bgcolor=black><p><b>총전투력:$katt</b><br>병종:$SOL_TYPE[$ksub1_ex]<br>훈련도:$kgat<br>지형상성:$SOL_TYPE1[$ksub1_ex]</td><td width=100 height=102  bgcolor=black><b>총전투력:$eatt</b><br>병종:$SOL_TYPE[$esub1_ex]<br>훈련도:$egat<br>지형상성:$SOL_TYPE1[$esub1_ex]</td></tr></table>");

										# --- v19 matchup/passive log (added; no deletions) ---
										if($kcounter != 0 || $ecounter != 0){
											&K_LOG2("병종 상성 : $SOL_TYPE[$ksub1_ex] vs $SOL_TYPE[$esub1_ex] (아군 $kcounter%, 적군 $ecounter%)");
											&E_LOG2("병종 상성 : $SOL_TYPE[$esub1_ex] vs $SOL_TYPE[$ksub1_ex] (아군 $ecounter%, 적군 $kcounter%)");
										}
										if($kpassive_msg ne ""){ &K_LOG2($kpassive_msg); &E_LOG2($kpassive_msg); }
										if($epassive_msg ne ""){ &K_LOG2($epassive_msg); &E_LOG2($epassive_msg); }
										# --- end v19 matchup/passive log ---





										$kche = 100;
										$eche = 100;
										$ilrand = int(rand(6));

								

										if($ilrand == 1){
										&K_LOG4("\[$old_date\]$ename(무력:$estrt 통솔:$eleat)님과 일기토를 시작!");
										&E_LOG4("\[$old_date\]$kname(무력:$kstrt 통솔:$kleat)님과 일기토를 시작!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 핏발날리는 전장에서 양군이 지켜보는 가운데 일기토 시작!</font>");

										if($kskill =~ /Gc/ && rand(100) < 50){
										&K_LOG4("<font color=red>1</font>합:$kname의 일섬 발동! $ename님은 중태가 되었습니다.");
										&E_LOG4("<font color=red>1</font>합:$kname의 일섬 발동! $ename님은 중태가 되었습니다.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : $kname의 일섬이 발동! $ename의 상태가 이상하다!</font>");
										$ego_ex += $kstrt*10;
										if($eqo_ex > 1800){
											$ego_ex = 1800;
										}
										$kpoint += int($kstrt/10);
										&ENEMY_INPUT;
										}else{
										for($count=1;$count<60;$count++){


										if($kche <= 0){last;}

										$kdmge = int((($kstrt+$kleat)/50)+rand(($kstrt+$kleat)/10));
										$edmge = int((($estrt+$eleat)/50)+rand(($estrt+$eleat)/10));

										if($kdmge < 1){
											$kdmge=1;	
										}

							

										$eche -= $kdmge;

										if($eche <= 0){
											&K_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
											$wine = 1;
										last;
										}
										
										if($edmge < 1){
											$edmge=1;	
										}

										$kche -= $edmge;

										if($kche <= 0){
											&K_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
											last;
										}
										&K_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
										}
										}

										if($wine){
										$ilgito = int(rand(5));
										if($ilgito == 0){
										$edmg = int($edmg*0.8);
										&K_LOG4("$ename님의 수비력이 약화되었습니다.");
										&E_LOG4("$ename님의 수비력이 약화되었습니다.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 일기토 결과, $ename의 패배가 확실시! 수비력이 약화!</font>");
										}elsif($ilgito == 1){
										if($egold < 1000){
										&K_LOG4("탈취하려고 했으나 $ename님이 돈이 1000미만입니다.");
										&E_LOG4("탈취당할뻔했으나 $ename님은 돈이 1000미만입니다.");
										}else{
										$goldt = int(rand(1000));
										$kgold += $goldt;
										$egold -= $goldt;
										&K_LOG4("$ename님에게서 금 $goldt를 탈취하였습니다.");
										&E_LOG4("$kname님에게 금 $goldt를 탈취당했습니다.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 일기토 결과, $ename의 패배가 확실시! 금 $goldt를 탈취당했다!</font>");
										}
										}elsif($ilgito == 2){
										$ego_ex += rand(100);
										&K_LOG4("$ename님에게 부상을 입혔습니다!");
										&E_LOG4("$kname님에게 부상을 당했습니다!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 일기토 결과, $ename의 패배가 확실시! 부상을 입었다!</font>");
										}else{
										&K_LOG4("일기토로 인해 아무 일이 없었습니다.");
										&E_LOG4("일기토로 인해 아무 일이 없었습니다.");
										}

										&MAP_LOG("<img src=$IMG/j25.gif> $kname님이 $ename님을 상대로 일기토에서 승리!");
										&K_LOG4("\[$old_date\]$kname님이 $ename님을 상대로 일기토에서 승리!");
										&E_LOG4("\[$old_date\]$kname님이 $ename님을 상대로 일기토에서 승리!");
										}else{

										$ilgito = int(rand(5));
										if($ilgito == 0){
										$kdmg = int($kdmg*0.8);
										&K_LOG4("$kname님의 공격력이 약화되었습니다.");
										&E_LOG4("$kname님의 공격력이 약화되었습니다.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 일기토 결과, $kname의 패배가 확실시! 수비력이 약화!</font>");
										}elsif($ilgito == 1){
										if($kgold < 1000){
										&E_LOG4("탈취하려고 했으나 $kname님이 돈이 1000미만입니다.");
										&K_LOG4("탈취당할뻔했으나 $kname님은 돈이 1000미만입니다.");
										}else{
										$goldt = int(rand(1000));
										$egold += $goldt;
										$kgold -= $goldt;
										&K_LOG4("$ename님에게 금 $goldt를 탈취당했습니다.");
										&E_LOG4("$kname님에게서 금 $goldt를 탈취하였습니다.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 일기토 결과, $kname의 패배가 확실시! 금 $goldt를 탈취당함!</font>");
										}
										}elsif($ilgito == 2){
										$go_ex += rand(100);
										&E_LOG4("$kname님에게 부상을 입혔습니다!");
										&K_LOG4("$ename님에게 부상을 당했습니다!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 일기토 결과, $kname의 패배가 확실시! 부상을 입었다!</font>");
										}else{
										&K_LOG4("일기토로 인해 아무 일이 없었습니다.");
										&E_LOG4("일기토로 인해 아무 일이 없었습니다.");
										}

										&MAP_LOG("<img src=$IMG/j25.gif> $ename님이 $kname님을 상대로 일기토에서 승리!");
										&K_LOG4("\[$old_date\]$ename님이 $kname님을 상대로 일기토에서 승리!");
										&E_LOG4("\[$old_date\]$ename님이 $kname님을 상대로 일기토에서 승리!");
										}

										}elsif($ilrand == 2){
										&K_LOG4("\[$old_date\]$ename(지력:$eintt 매력:$echat)님과 설전을 시작!");
										&E_LOG4("\[$old_date\]$kname(지력:$kintt 매력:$kchat)님과 설전을 시작!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 양쪽 군세에서 장수들이 나와 호통을 치기 시작했다!</font>");
										for($count=1;$count<60;$count++){

										if($kche <= 0){last;}

										$kdmge = int((($kintt+$kchat)/50)+rand(($kintt+$kchat)/10));
										$edmge = int((($eintt+$echat)/50)+rand(($eintt+$echat)/10));

										if($kdmge < 1){
											$kdmge=1;	
										}

							

										$eche -= $kdmge;

										if($eche <= 0){
											$eche = 0;
											&K_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
											$wine = 1;
										last;
										}
										
										if($edmge < 1){
											$edmge=1;	
										}

										$kche -= $edmge;

										if($kche <= 0){
											$kche = 0;
											&K_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
											last;
										}
										&K_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
										}

										if($wine){
										$ilgito = int(rand(5));
										if($ilgito == 0){
										$edmg = int($edmg*0.8);
										&K_LOG4("$ename님의 수비력이 약화되었습니다.");
										&E_LOG4("$ename님의 수비력이 약화되었습니다.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 설전 결과, $ename의 패배가 확실시! 수비력이 약화!</font>");
										}elsif($ilgito == 1){
										if($egold < 1000){
										&K_LOG4("탈취하려고 했으나 $ename님이 돈이 1000미만입니다.");
										&E_LOG4("탈취당할뻔했으나 $ename님은 돈이 1000미만입니다.");
										}else{
										$goldt = int(rand(1000));
										$kgold += $goldt;
										$egold -= $goldt;
										&K_LOG4("$ename님에게서 금 $goldt를 탈취하였습니다.");
										&E_LOG4("$kname님에게 금 $goldt를 탈취당했습니다.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 설전 결과, $ename의 패배가 확실시! 금 $goldt를 탈취당함!</font>");
										}
										}elsif($ilgito == 2){
										$ego_ex += rand(100);
										&K_LOG4("$ename님에게 부상을 입혔습니다!");
										&E_LOG4("$kname님에게 부상을 당했습니다!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 설전 결과, $ename의 패배가 확실시! 부상을 당함!</font>");
										}else{
										&K_LOG4("설전으로 인해 아무 일이 없었습니다.");
										&E_LOG4("설전으로 인해 아무 일이 없었습니다.");
										}

										&MAP_LOG("<img src=$IMG/j26.gif> $kname님이 $ename님을 상대로 설전에서 승리!");
										&K_LOG4("\[$old_date\]$kname님이 $ename님을 상대로 설전에서 승리!");
										&E_LOG4("\[$old_date\]$kname님이 $ename님을 상대로 설전에서 승리!");
										}elsif(!$wine){
										$ilgito = int(rand(5));
										if($ilgito == 0){
										$kdmg = int($kdmg*0.8);
										&K_LOG4("$kname님의 공격력이 약화되었습니다.");
										&E_LOG4("$kname님의 공격력이 약화되었습니다.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 설전 결과, $kname의 패배가 확실시! 공격력이 약화!</font>");
										}elsif($ilgito == 1){
										if($kgold < 1000){
										&E_LOG4("탈취하려고 했으나 $kname님이 돈이 1000미만입니다.");
										&K_LOG4("탈취당할뻔했으나 $kname님은 돈이 1000미만입니다.");
										}else{
										$goldt = int(rand(1000));
										$egold += $goldt;
										$kgold -= $goldt;
										&K_LOG4("$ename님에게 금 $goldt를 탈취당했습니다.");
										&E_LOG4("$kname님에게서 금 $goldt를 탈취하였습니다.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 설전 결과, $kname의 패배가 확실시! 금 $goldt를 탈취당함!</font>");
										}
										}elsif($ilgito == 2){
										$go_ex += rand(100);
										&E_LOG4("$kname님에게 부상을 입혔습니다!");
										&K_LOG4("$ename님에게 부상을 당했습니다!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : 설전 결과, $kname의 패배가 확실시! 부상을 당함!</font>");
										}else{
										&K_LOG4("설전으로 인해 아무 일이 없었습니다.");
										&E_LOG4("설전으로 인해 아무 일이 없었습니다.");
										}
										&MAP_LOG("<img src=$IMG/j26.gif> $ename님이 $kname님을 상대로 설전에서 승리!");
										&K_LOG4("\[$old_date\]$ename님이 $kname님을 상대로 설전에서 승리!");
										&E_LOG4("\[$old_date\]$ename님이 $kname님을 상대로 설전에서 승리!");
										}
										}

									}


										open(IN,"./charalog/command1/$kid\.cgi");
										@KCOM = <IN>;
										close(IN);

										open(IN,"./charalog/command1/$eid\.cgi");
										@ECOM = <IN>;
										close(IN);
									

										$W_JEN_SUL[1] = 10;
										$W_JEN_SUL[2] = 10;
										$W_JEN_SUL[3] = 10;
										$W_JEN_SUL[4] = 15;
										$W_JEN_SUL[5] = 15;
										$W_JEN_SUL[6] = 15;
										$W_JEN_SUL[11] = 28;
										$W_JEN_SUL[12] = 18;
										$W_JEN_SUL[13] = 22;
										$W_JEN_SUL[14] = 20;
										$W_JEN_SUL[15] = 15;
										$W_JEN_SUL[16] = 15;
										$W_JEN_SUL[18] = 40;

										$L_JEN_SUL[1] = -10;
										$L_JEN_SUL[2] = -10;
										$L_JEN_SUL[3] = -10;
										$L_JEN_SUL[4] = -12;
										$L_JEN_SUL[5] = -12;
										$L_JEN_SUL[6] = -12;
										$L_JEN_SUL[11] = -15;
										$L_JEN_SUL[12] = -12;
										$L_JEN_SUL[13] = -15;
										$L_JEN_SUL[14] = -12;
										$L_JEN_SUL[15] = -12;
										$L_JEN_SUL[16] = -8;
										$L_JEN_SUL[18] = -25;


										$gg = 0;
										for($count=0;$count<30;$count++){
										$gg++;
				
										if(($karm != 17 && $kcno == 11) || ($ksub1_ex != 5 && $kcno == 14) || ($ksub1_ex != 7 && $kcno == 16) || ($ksub1_ex != 11 && $kcno == 15) || ($karm != 18 && $kcno == 12) || ($karm != 19 && $kcno == 13)){
											$kcno = 0;
											$kccp = 0;
											$krap = 0;
										}
										if(($earm != 17 && $ecno == 11) || ($esub1_ex != 5 && $ecno == 14) || ($esub1_ex != 7 && $ecno == 16) || ($esub1_ex != 11 && $ecno == 15) || ($earm != 18 && $ecno == 12) || ($earm != 19 && $ecno == 13)){
											$ecno = 0;
											$eccp = 0;
											$erap = 0;
										}
										if($ksol <= 0){last;}

										if($last_battle eq "0"){
										($kcname,$kcno,$kccp,$krap) = split(/<>/,$KCOM[$count]);
										($ecname,$ecno,$eccp,$erap) = split(/<>/,$ECOM[$count]);

				

										if($krap == 0 && ($erap == 1 || $erap == 2 || $erap == 3)){
										$flag = "◀";
										$kjensul = -20;
										$ejensul = $W_JEN_SUL[$ecno];
										}elsif($erap == 0 && ($krap == 1 || $krap == 2 || $krap == 3)){
										$flag = "▶";
										$kjensul = $W_JEN_SUL[$kcno];
										$ejensul = -20;
										}elsif(($krap == 0 && $erap == 0) || ($krap == 1 && $erap == 1) || ($krap == 2 && $erap == 2) || ($krap == 3 && $erap == 3)){
										$flag = "〓";
										$kjensul = 0;
										$ejensul = 0;
										}elsif(($krap == 1 && $erap == 2) || ($krap == 2 && $erap == 3) || ($krap == 3 && $erap == 1)){
										if($esub1_ex == 7 && $ecno == 16){
											$esol += 200;
											&K_LOG3("<font color=red>$count</font>턴:원공진 발동! 적군의 병사가 <font color=blue>+200</font> 상승!");
											&E_LOG3("<font color=red>$count</font>턴:원공진 발동! 아군의 병사가 <font color=blue>+200</font> 상승!");
										}
										if($earm == 18 && $ecno == 12){
											$edamage = int($katt * 0.4);
											&K_LOG3("<font color=red>$count</font>턴:비천진 발동! 아군의 공격력이 <font color=blue>$edamage</font> 감소!");
											&E_LOG3("<font color=red>$count</font>턴:비천진 발동! 적의 공격력이 <font color=blue>$edamage</font> 감소!");
										}
										$flag = "◀";
										$kjensul = $L_JEN_SUL[$kcno];
										$ejensul = $W_JEN_SUL[$ecno];
										}elsif(($erap == 1 && $krap == 2) || ($erap == 2 && $krap == 3) || ($erap == 3 && $krap == 1)){
										if($ksub1_ex == 11 && $kcno == 15){
											$egat -= 10;
											&K_LOG3("<font color=red>$count</font>턴:신라검진 발동! 적 장수의 훈련도를 깎았다!");
											&E_LOG3("<font color=red>$count</font>턴:신라검진 발동! 적 장수에게 훈련도를 깎였다!");
										}
										if($karm == 19 && $kcno == 13){
											$ego_ex += 70;
											&K_LOG3("<font color=red>$count</font>턴:탄망진 발동! 적 장수에게 상처를 입혔다!");
											&E_LOG3("<font color=red>$count</font>턴:탄망진 발동! 적 장수에게 상처를 입었다!");
										}
										$flag = "▶";
										$kjensul = $W_JEN_SUL[$kcno];
										$ejensul = $L_JEN_SUL[$ecno];
										}
										$kdmg = int((rand($katt*1.5) - $edamage) * (($SOL_TYPE1[$ksub1_ex]+$kjensul)/100));
										$edmg = int(rand($eatt*1.5)*(($SOL_TYPE1[$esub1_ex]+$ejensul)/100));

										$kjihyng = int($SOL_TYPE1[$ksub1_ex]+$kjensul);
										$ejihyng = int($SOL_TYPE1[$esub1_ex]+$ejensul);

										}elsif($last_battle eq "1"){
										$flag = "VS";
										$kdmg = int(rand($katt*2)+$kdmg1);
										$edmg = int(rand($eatt*2)+$edmg1);

										$padmg = int(5+rand(5));
										if($ksub1_ex == 17 && $last_battle == 1){
										$zdef_att -= $padmg;
										$gmd = "/방어시설 $zdef_att(-$padmg\)";
										}
										}
										


										if(($kdmg eq ""  || $kdmg < 1) && $ksuk < 1){
											$kdmg=1;	
										}elsif($kdmg < $ksuk){
										if($ksuk > $katt){
										$kdmg=$katt;}else{$kdmg=$ksuk;}
										}
										$wsol = $esol;
										$esol -= $kdmg;
										

										if($last_battle eq "0"){
										$kex_add += ($wsol - $esol);
										}elsif($last_battle eq "1"){
										$kex_add += int(($wsol - $esol)/5);
										}
										
										if($esol <= 0){
											$esol=0;
											&K_LOG3("<font color=red>$count</font>턴:$kname의 $SOL_TYPE[$ksub1_ex]부대 $ksol명 (-$edmg\)$kjihyng $flag $ename의 $SOL_TYPE[$esub1_ex]부대 $esol명 (-$kdmg\)$gmd$kskilldmg$ejihyng");
											&E_LOG3("<font color=red>$count</font>턴:$kname의 $SOL_TYPE[$ksub1_ex]부대 $ksol명 (-$edmg\)$kjihyng $flag $ename의 $SOL_TYPE[$esub1_ex]부대 $esol명 (-$kdmg\)$ejihyng");
											$win = 1;
										last;
										}
										
										if(($edmg eq "" || $edmg < 1) && $esuk < 1){
											$edmg=1;	
										}elsif($edmg < $esuk){
										if($esuk > $eatt){
										$edmg=$eatt;}else{$edmg=$esuk;}
										}
										$wsol = $ksol;
										$ksol -= $edmg;
										$eex_add += ($wsol - $ksol);
										if($ksol <= 0){
											$ksol=0;
											&K_LOG3("<font color=red>$count</font>턴:$kname의 $SOL_TYPE[$ksub1_ex]부대 $ksol명 (-$edmg\)$kjihyng $flag $ename의 $SOL_TYPE[$esub1_ex]부대 $esol명 (-$kdmg\)$gmd$kskilldmg$ejihyng");
											&E_LOG3("<font color=red>$count</font>턴:$kname의 $SOL_TYPE[$ksub1_ex]부대 $ksol명 (-$edmg\)$kjihyng $flag $ename의 $SOL_TYPE[$esub1_ex]부대 $esol명 (-$kdmg\)$ejihyng");
											last;
										}

										&K_LOG3("<font color=red>$count</font>턴:$kname의 $SOL_TYPE[$ksub1_ex]부대 $ksol명 (-$edmg\)$kjihyng $flag $ename의 $SOL_TYPE[$esub1_ex]부대 $esol명 (-$kdmg\)$gmd$kskilldmg$ejihyng");
									}

									$eex_add = int($eex_add/40);
									$kex_add = int($kex_add/40);
									$kex_add1 = int($kex_add/350);
									$eex_add1 = int($eex_add/350);
									if($win){
										$ksub2_ex++;
										if($last_battle){
											if($town_get[$zcon] <= 1){
												@NEW_COU=();
												foreach(@COU_DATA){
													($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
													if("$zcon" eq "$xcid"){
													}else{
														push(@NEW_COU,"$_");
													}
												}
												open(OUT,">$COUNTRY_LIST");
												print OUT @NEW_COU;
												close(OUT);
												&MAP_LOG2("<img src=$IMG/j3.gif> \[$old_date\]$cou_name[$zcon]국은 멸망했습니다.");
												&MAP_LOG("<img src=$IMG/j3.gif> \[$old_date\]$cou_name[$zcon]국은 멸망했습니다.");
											}


											$zcon = $kcon;
											$znou = int($znou*0.8);
											$zsyo = int($zsyo*0.8);
											$zsub1 = int($zsub1*0.8);
											$zshiro += 100;
											$zpri = int($zpri*0.8);
											$zdef_att = int($zdef_att*0.8);
											$zbong1 = "";
											$zbong2 = "";
											$zbong3 = "";
											$kex_add += 80;
											$kcex += $kex_add;
											$kexp += $kex_add;
											$kpoint += $kex_add1;
											$kpos = $cnum;

											@NEW_DEF_LIST3=();
											$pphit=0;
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef) = split(/<>/);
												if("$did" eq "$kid"){
													$pphit=1;													unshift(@NEW_DEF_LIST3,"$kid<>$kname<>$kpos<>0<>$kcon<>$kchara<>$ksol<>$ksub1_ex<>0<>\n");
												}else{
													push(@NEW_DEF_LIST3,"$_");
												}
											}


											if(!$pphit){
												unshift(@NEW_DEF_LIST3,"$kid<>$kname<>$kpos<>0<>$kcon<>$kchara<>$ksol<>$ksub1_ex<>0<>\n");
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);



											&K_LOG2("<font color=blue>$zname</font>를 손에 넣었다! <font color=red>$kex_add</font>의 공헌치를 얻었습니다!");
											&HISTORY_LOG($kid,"<font color=blue>$zname</font>를 손에 넣었다!");
											&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : $kname의 부대가 $zname성을 점령했다!</font>");
											&MAP_LOG2("<img src=$IMG/j4.gif> \[$old_date\]$cou_name[$kcon]국의 $kname부대는 $zname성을 점령했습니다!");
											&MAP_LOG("<img src=$IMG/j4.gif> $cou_name[$kcon]국의 $kname부대는 $zname를 점령했습니다!");
										}else{
											@NEW_DEF_LIST3=();
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef) = split(/<>/);
												if("$mdid" ne "$did"){
													push(@NEW_DEF_LIST3,"$_");
												}
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /전쟁/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth월 : $qtalkd");
										}
										}
									}	
								}
							}

											$kex_add += 50;
											$eex_add += 15;
											$kcex += int($kex_add * 0.8);
											$kexp += int($kex_add * 0.8);
											$kgg = int($kex_add * 0.8);
											$kpoint += $kex_add1;
											$ecex += int($eex_add * 0.6);
											$eexp += int($kex_add * 0.6);
											$egg = int($eex_add * 0.6);
											$epoint += $eex_add1;
											$esol = 0;
											$egat = 0;
											$kqpoint += 1 if $kcodea =~ /A9|C8/;
											&K_LOG2("\[$old_date\] $kname의 $SOL_TYPE[$ksub1_ex]부대는 $ename의 $SOL_TYPE[$esub1_ex]부대를 전멸시켰습니다! <font color=blue>$kgg</font>의 공헌치를 얻었습니다!");
											&E_LOG2("\[$old_date\] $ename의 $SOL_TYPE[$esub1_ex]부대는 $kname의 $SOL_TYPE[$ksub1_ex]부대에게 패배했다. <font color=red>$egg</font>의 공헌치를 얻었습니다!");
											&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : $kname의 부대는 요격중이던 $ename의 부대를 파죽지세로 전멸시킨 모양이다.</font>");
											&MAP_LOG("<img src=$IMG/j5.gif> $kname의 $SOL_TYPE[$ksub1_ex]부대는 $ename의 $SOL_TYPE[$esub1_ex]부대를 전멸시켰습니다!");
										}
									}else{
											$esub2_ex++;
											@NEW_DEF_LIST3=();
											$dnum = 0;
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef) = split(/<>/);
												if("$kid" ne "$did"){
													push(@NEW_DEF_LIST3,"$_");
												}
												if($eid eq "$did"){
													$ddef++;
													splice(@NEW_DEF_LIST3,$dnum,1,"$did<>$dname<>$dtown_id<>$dtown_flg<>$dcon<>$dchara<>$esol<>$dsub1_ex<>1<>$ddef<>\n");
												}
												$dnum++;
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($ecodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /전쟁/){
										$eqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&E_LOG("$mmonth월 : $qtalkd");
										}
									}	
								}
							}

										$eex_add += 50;
										$kex_add += 15;
										$ecex += $eex_add;
										$kcex += $kex_add;
										$eexp += $eex_add;
										$kexp += $kex_add;
										$epoint += $eex_add1;
										$kpoint += $kex_add1;
										if($gg < 30){
										$kgat = 0;
										}
										&K_LOG2("\[$old_date\] $kname의 $SOL_TYPE[$ksub1_ex]부대는 $ename의 $SOL_TYPE[$esub1_ex]부대에게 패배했다.. <font color=red>$kex_add</font>의 공헌치를 얻었습니다!");
										&E_LOG2("\[$old_date\] $ename의 $SOL_TYPE[$esub1_ex]부대는 $kname의 $SOL_TYPE[$ksub1_ex]부대를 전멸시켰다!! <font color=blue>$eex_add</font>의 공헌치를 얻었습니다!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth월 : $ename의 부대는 공격해 들어오는 $kname의 부대를 요격으로 전멸시킨 모양이다.</font>");
									}

									if(!$last_battle){
										if($eid ne ""){
											&ENEMY_INPUT;
										}
									}else{
										$zshiro = $esol;
										if($ksub1_ex eq "12"){
										$zdef_att -= int($ksol/50);
										}else{
										$zdef_att -= int($ksol/100);
										}
										if($zdef_att < 0){
											$zdef_att=0;
										}
											splice(@TOWN_DATA,$cnum,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
									}


									&BATTLE_LOG("<HR NOSHADE SIZE=3>");
									$kstr_ex++;
									$go_ex += int($kbank/5);
									$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
								}
							}
						}	
}
1;

