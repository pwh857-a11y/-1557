#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("로딩중입니다. 잠깐 기다려 주세요."); }
&DECODE;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("주소 바에 값을 입력하지 말아주세요."); }
if($mode eq 'QUEST2') { require './quest/quest2.cgi';&QUEST2; }
elsif($mode eq 'QUEST') { require './quest/quest.cgi';&QUEST; }
elsif($mode eq 'QUEST3') { require './quest/quest3.cgi';&QUEST3; }
elsif($mode eq 'QUEST4') { require './quest/quest4.cgi';&QUEST4; }
elsif($mode eq 'QUEST5') { require './quest/quest5.cgi';&QUEST5; }
else{&ERR('올바르게 선택되지 않았습니다.');}