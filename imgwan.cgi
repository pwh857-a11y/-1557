
sub IMGWAN{
						$ksub2=0;
						&CON_NUM;
						&COUNTRY_DATA_OPEN($kcon);


						$timelimit = $F_YEAR+$myear;

						if($xcid eq 0){
							if($cou_name[$cnum] eq ""){
								&K_LOG("$mmonth월 : 그 나라에 등용될 수 없습니다.");
							}elsif($timelimit < 184 && $connum1 >= 20){
								&K_LOG("$mmonth월 : 184년 1월 전까지는 $cou_name[$cnum]국에 임관할 수 없습니다.");
							}else{
								if(@B_LIST eq "0"){
									open(IN,"./log_file/black_list.cgi");
									@B_LIST = <IN>;
									close(IN);
								}
								$b_hit=0;
								foreach(@B_LIST){
									($bid,$bcon,$bname,$bsub) = split(/<>/);
									if($bid eq $kid && $bcon eq $kcon){
										$b_hit=1;
									}
								}
								if($b_hit){
									&K_LOG("$mmonth월 : $cou_name[$cnum]국에서 임관이 거부되었습니다.");
								}else{	
				
									$kcon = $cnum;
									&K_LOG("$mmonth월 : $cou_name[$cnum]에 임관했습니다.");
									&HISTORY_LOG($kid,"$cou_name[$cnum]에 임관했습니다.");
									&MAP_LOG("<img src=$IMG/j2.gif> $kname님은 $cou_name[$cnum]국으로 임관했습니다.");
								}
							}
						}else{
							&K_LOG("$mmonth월 : 재야가 아니면 등용될 수가 없습니다.");
						}
}
1;

