#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';
if($MENTE) { &ERR2("로딩중입니다. 잠시만 기다려주세요."); }
&DECODE;
&SERVER_STOP;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("주소창에 값을 입력하지 말아주세요."); }



if($mode eq '0') { require 'command/none.cgi';&NONE;}
elsif($mode eq '1') { require 'command/nougyou.cgi';&NOUGYOU; }
elsif($mode eq '2')  { require 'command/syougyou.cgi';&SYOUGYOU; }
elsif($mode eq '3')  { require 'command/shiro.cgi';&SHIRO; }
elsif($mode eq '4')  { require 'command/all_nou.cgi';&ALL_NOU; }
elsif($mode eq '5')  { require 'command/all_syo.cgi';&ALL_SYO; }
elsif($mode eq '6')  { require 'command/all_shiro.cgi';&ALL_SHIRO; }
elsif($mode eq '7')  { require 'command/all_kunren.cgi';&ALL_KUNREN; }
elsif($mode eq '8')  { require 'command/rice_give.cgi';&RICE_GIVE; }
elsif($mode eq '9')  { require 'command/get_sol.cgi';&GET_SOL; }
elsif($mode eq '10') { require 'command/get_sol2.cgi';&GET_SOL2; }
elsif($mode eq '11') { require 'command/kunren.cgi';&KUNREN; }
elsif($mode eq '12') { require 'command/town_def.cgi';&TOWN_DEF; }
elsif($mode eq '13') { require 'command/battle.cgi';&BATTLE; }
elsif($mode eq '14') { require 'command/buy.cgi';&BUY; }
elsif($mode eq '15') { require 'command/arm_buy.cgi';&ARM_BUY; }
elsif($mode eq '16') { require 'command/def_buy.cgi';&DEF_BUY; }
elsif($mode eq '17') { require 'command/move.cgi';&MOVE; }
elsif($mode eq '18') { require 'command/battle2.cgi';&BATTLE2; }
elsif($mode eq '19') { require 'command/buy2.cgi';&BUY2; }
elsif($mode eq '20') { require 'command/move2.cgi';&MOVE2; }
elsif($mode eq '21') { require 'command/shikan.cgi';&SHIKAN; }
elsif($mode eq '22') { require 'command/arm_buy2.cgi';&ARM_BUY2; }
elsif($mode eq '23') { require 'command/def_buy2.cgi';&DEF_BUY2; }
elsif($mode eq '24') { require 'command/get_man.cgi';&GET_MAN; }
elsif($mode eq '25') { require 'command/get_man2.cgi';&GET_MAN2; }
elsif($mode eq '26') { require 'command/tanren.cgi';&TANREN; }
elsif($mode eq '27') { require 'command/tanren2.cgi';&TANREN2; }
elsif($mode eq '28') { require 'command/syuugou.cgi';&SYUUGOU; }
elsif($mode eq '29') { require 'command/tec.cgi';&TEC; }
elsif($mode eq '30') { require 'command/shiro_tai.cgi';&SHIRO_TAI; }
elsif($mode eq '31') { require 'command/kunren_hard.cgi';&KUNREN_HARD; }
elsif($mode eq '32') { require 'command/choto.cgi';&CHOTO; }
elsif($mode eq '33') { require 'command/hakai.cgi';&HAKAI; }
elsif($mode eq '34') { require 'command/hakai2.cgi';&HAKAI2; }
elsif($mode eq '35') { require 'command/ryugen.cgi';&RYUGEN; }
elsif($mode eq '36') { require 'command/ryugen2.cgi';&RYUGEN2; }
elsif($mode eq '37') { require 'command/yakiuchi.cgi';&YAKIUCHI; }
elsif($mode eq '38') { require 'command/yakiuchi2.cgi';&YAKIUCHI2; }
elsif($mode eq '39') { require 'command/hataage.cgi';&HATAAGE; }
elsif($mode eq '40') { require 'command/geya.cgi';&GEYA; }
elsif($mode eq '41') { require 'command/hataage2.cgi';&HATAAGE2; }
elsif($mode eq '44') { require 'command/yusou.cgi';&YUSOU; }
elsif($mode eq '66') { require 'command/yusou.cgi';&YUSOU12; }
elsif($mode eq '45') { require 'command/yusou.cgi';&YUSOU2; }
elsif($mode eq '46') { require 'command/zenjou.cgi';&ZENJOU; }
elsif($mode eq '47') { require 'command/zenjou.cgi';&ZENJOU2; }
elsif($mode eq '43') { require 'command/tansaku.cgi';&TANSAKU; }
elsif($mode eq '48') { require 'command/dokuritsu.cgi';&DOKURITSU; }
elsif($mode eq '49') { require 'command/dokuritsu.cgi';&DOKURITSU2; }
elsif($mode eq '50') { require 'command/trap.cgi';&HIWANA; }
elsif($mode eq '51') { require 'command/trap.cgi';&RAKUSEKI; }
elsif($mode eq '52') { require 'command/trap.cgi';&KYOHOU; }
elsif($mode eq '53') { require 'command/bal.cgi';&BAL; }
elsif($mode eq '54') { require 'command/bal.cgi';&BAL2; }
elsif($mode eq '67') { require 'command/bal.cgi';&BAL12; }
elsif($mode eq '55') { require 'command/skill_buy.cgi';&SKILL_BUY; }
elsif($mode eq '56') { require 'command/skill_buy2.cgi';&SKILL_BUY2; }
elsif($mode eq '57') { require './battle_entry.pl';&battle_entry; }
elsif($mode eq '58') { require 'command/money_send.cgi';&MONEY_SEND; }
elsif($mode eq '59') { require 'command/money_send2.cgi';&MONEY_SEND2; }
elsif($mode eq '60') { require 'command/sangjem.cgi';&SANGJEM; }
elsif($mode eq '61') { require 'command/husik.cgi';&HUSIK; }
elsif($mode eq '62') { require 'command/ilgi.cgi';&ILGI; }
elsif($mode eq '63') { require 'command/ilgi2.cgi';&ILGI2; }
elsif($mode eq '64') { require 'command/husik2.cgi';&HUSIK2; }
elsif($mode eq '65') { require 'command/husik3.cgi';&HUSIK3; }
elsif($mode eq '68') { require 'command/nongmove.cgi';&NONGMOVE; }
elsif($mode eq '69') { require 'command/nongmove.cgi';&NONGMOVE2; }
elsif($mode eq '70') { require 'command/nongmove.cgi';&NONGMOVE3; }
elsif($mode eq '100') { require 'command/chamga.cgi';&CHAMGA; }
else { &ERR("올바르지 않은 엑세스입니다."); }

