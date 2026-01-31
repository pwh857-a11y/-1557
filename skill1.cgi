
sub SKILL1{
$ksub2=0;
open(IN,"$SKILL_LIST");
@SKILL_DATA = <IN>;
close(IN);
($dk,$eskillcode,$eskillpoint) = split(/<>/,$SKILL_DATA[$cnum]);
&SKILL;
if($eskillpoint > $kpoint){
&K_LOG("$mmonth월 : $name을 배우기에는 스킬포인트가 충분하지 않습니다. (필요SP : $eskillpoint)");
}else{
$kqpoint = 1 if $kcodea =~ /C9/;
$kpoint -= $eskillpoint;
$kskill .= $eskillcode;
&K_LOG("$mmonth월 : 특기 $name를 배웠습니다.");
&MAP_LOG("<img src=$IMG/j24.gif> $kname님은 $name을 배웠습니다.");
}
}
1;

