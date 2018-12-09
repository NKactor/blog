
<!--
var pager = new ETNGpager('list','list2',24,10);//24ÎªÃ¿Ò³ÏÔÊ¾ÌõÊý¡£10Îªµ¼º½ÏÔÊ¾²Ëµ¥Êý
var curP = 1;
page()
function page(i){
curP =(curP>pager.cntP)?1:curP;
if(i){
curP = n =i;
}else{
n = curP++;
}
pager.curP = (n>pager.cntP)?pager.cntP:n;
pager.create();
}
//-->
