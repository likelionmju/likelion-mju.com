$(document).ready(function(){
    var deadline = new Date(2020,2,19,18,0,0,0);
    var now = new Date();
    if (now > deadline){
        alert("서류지원이 마감되었습니다.");
        $('#apply').bind('click', false);
    }
});