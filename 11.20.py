Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
import urllib2

 

>>> page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
>>> try:
	request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        
  File "<pyshell#3>", line 4
    response = urllib2.urlopen(request)
                                      ^
IndentationError: unindent does not match any outer indentation level
>>> 
>>> 

line 373, in _read_status
 raise BadStatusLine(line)
httplib.BadStatusLine: ''
1
2
3
line 373, in _read_status
 raise BadStatusLine(line)
httplib.BadStatusLine: ''
SyntaxError: invalid syntax
>>> 
>>> import urllib
>>> import urllib2
>>> page = 1
>>> url = 'http://www.qiushibaike.com/hot/page/' + str(page)
>>> user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
>>> headers = { 'User-Agent' : user_agent }
>>> try:
	request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        
  File "<pyshell#14>", line 4
    response = urllib2.urlopen(request)
                                      ^
IndentationError: unindent does not match any outer indentation level
>>> request = urllib2.Request(url,headers = headers)
>>> response = urllib2.urlopen(request)
>>> print response.read()
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="X-UA-Compatible" content="chrome=1,IE=edge">
<meta name="renderer" content="webkit"/>
<meta name="applicable-device" content="pc">


















<title>24Сʱ��ЦЦ����ȫ - ���°ٿ�</title>






















<meta name="keywords" content="Ц��,Ц����ȫ" />
<meta name="description" content="���°ٿƹ����ṩ24Сʱ���ܸ�ЦЦ����ȫ,�ܰ�24Сʱ�����������¾�ֻ�����°ٿƹ���24Сʱר��,������㡢���������¾���,���ּ�ѹ��"/>
<meta http-equiv="mobile-agent" content="format=xhtml;url=//www.qiushibaike.com/hot/">
<meta http-equiv="mobile-agent" content="format=html5;url=//www.qiushibaike.com/hot/">



<meta name="robots" content="noarchive">
<link href="//static.qiushibaike.com/css/dist/web/app.min.css?v=fd76de5efd22f0f804665ba809048729" media="screen, projection" rel="stylesheet" type="text/css"/>
<script type="text/javascript">
// Baidu Automatic push content
var _hmt = _hmt || [];
(function() {
var hm = document.createElement("script");
hm.src = "https://hm.baidu.com/hm.js?2670efbdd59c7e3ed3749b458cafaa37";
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(hm, s);
})();
// �ռ���Ӫ�ϻ���֤��
window.config = {
'user_time': '2017-11-20 10:35:25',
'version': '2017-09-04 14:36'
}
</script>
</head>
<body>



<div id="header" class="head">
<div class="content-block">
<div class="logo" id="hd_logo">
<a href="/"><h1>���°ٿ�</h1></a>
</div>
<div id="menu" class="menu-bar menu clearfix" style="margin:0 10px">
<a  href="/" rel="nofollow">����</a>
<a  id="highlight"  href="/hot/">24Сʱ</a>
<a  href="/imgrank/">��ͼ</a>
<a  href="/text/">����</a>
<a  href="/history/">��Խ</a>
<a  href="/pic/">��ͼ</a>
<a  href="/textnew/">����</a>
<a  class="fn-signin-required" href="javascript:void(0);" data-go="/article/add" rel="nofollow">Ͷ��</a>
<!--<a href="http://www.youliaodao.cn" target="_blank" rel="nofollow">�ٿ�</a>-->
</div>
<div class="userbar clearfix">
<div class="login hidden">
<a href="/my" class="username" id="uname" rel="nofollow"></a>
</div>
<div class="logout">
<a href="javascript:void(0);" class="fn-signin-required logintop" id='logintop' rel="nofollow" style="font-size:16.5px;">��¼</a>
</div>
</div>
</div>
</div>



<div id="content" class="main">
<div class="content-block clearfix">

<div id="content-left" class="col1">








<div class="article block untagged mb15 typs_long" id='qiushi_tag_119742381'>


<div class="author clearfix">
<span style="height: 35px">
<img src="//static.qiushibaike.com/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87" alt="�����û�">
</span>
<span>
<h2>�����û�</h2>
</span>
<!-- <div class="articleGender manIcon">32</div> -->
</div>

<a href="/article/119742381" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


�������£��������Һܸп�������28��������˺��ӣ�������Ϊ���˺��ӻ�û�����ر��鷳���Ҽҵ����ż�û�г�����������5�����˸����ֳ�������������쵽����Ҫ��תһ�£������Ҹ磬������ϵ�ܺõ����ѣ�֪�������У����ǿ��ڶ�˵û�У�ֻ����һ����ϵһ��㣬���ǱȽϺ�˵�������ѿ��ڣ�������˵��ת�����ˣ����һ�������Ա�������ʵ�Ǯ��ֻ����˵��������ǰ�����ͺã�Ϊ�����±����˺ܾã�ͦ��л���ģ���������˵���Ѳ���Ҫ�࣬��һ�����׵ľ͹��ˣ��ǳ���л����

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">566</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119742381" data-share="/article/119742381" id="c-119742381" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">49</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119742381" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119742381" class="up">
<a href="javascript:voting(119742381,1)" class="voting" data-article="119742381" id="up-119742381" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">578</span>
</a>
</li>
<li id="vote-dn-119742381" class="down">
<a href="javascript:voting(119742381,-1)" class="voting" data-article="119742381" id="dn-119742381" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-12</span>
</a>
</li>
<li class="comments">
<a href="/article/119742381" id="c-119742381" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119764926'>


<div class="author clearfix">
<a href="/users/30107945/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3010/30107945/thumb/20171111121842.JPEG?imageView2/1/w/90/h/90" alt="���˵�è*">
</a>
<a href="/users/30107945/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
���˵�è*
</h2>
</a>
<div class="articleGender manIcon">101</div>
</div>

<a href="/article/119764926" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


���п��Գɼ������ˣ�������绰ѵ���ӣ�������������ơ�<br/>����ս��ڵĵ¹����豸�ֱ�.���ˣ��������侯�Ѵ�����<br/>���ְ�...�ְ�...���绰��ͷ��������������...���㱻��.���Χ�ˣ������ز����˶���...��~Ү������

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">960</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119764926" data-share="/article/119764926" id="c-119764926" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">15</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119764926" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119764926" class="up">
<a href="javascript:voting(119764926,1)" class="voting" data-article="119764926" id="up-119764926" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">977</span>
</a>
</li>
<li id="vote-dn-119764926" class="down">
<a href="javascript:voting(119764926,-1)" class="voting" data-article="119764926" id="dn-119764926" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/119764926" id="c-119764926" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119764926" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">����轣�����ӡ���</span>
<div class="main-text">
¥��������˰ɣ�˵�����ǵڼ��� �� �
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


15

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119765011'>


<div class="author clearfix">
<a href="/users/5018907/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/501/5018907/thumb/20171119214649.JPEG?imageView2/1/w/90/h/90" alt="ѩ����...">
</a>
<a href="/users/5018907/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
ѩ����...
</h2>
</a>
<div class="articleGender womenIcon">30</div>
</div>

<a href="/article/119765011" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


����ϲ��������ץ��ɮ����Ϸ��ÿ�ζ��Ƕ�������գ��Ϲ�����ɮ���������֡�<br/>���죬�Ҳ����ˣ���Ҫ����ɮ......<br/>�����������ݣ�����Σ�����������ǣ�����ɮ����Ѻ�������쵰��û���ҵ����˭�������ˣ��������ˡ�<br/><br/>С������......��������ô����

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">1073</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119765011" data-share="/article/119765011" id="c-119765011" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">30</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119765011" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119765011" class="up">
<a href="javascript:voting(119765011,1)" class="voting" data-article="119765011" id="up-119765011" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1091</span>
</a>
</li>
<li id="vote-dn-119765011" class="down">
<a href="javascript:voting(119765011,-1)" class="voting" data-article="119765011" id="dn-119765011" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-18</span>
</a>
</li>
<li class="comments">
<a href="/article/119765011" id="c-119765011" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119750485'>


<div class="author clearfix">
<a href="/users/33694723/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3369/33694723/thumb/20171110211954.JPEG?imageView2/1/w/90/h/90" alt="�����Ա">
</a>
<a href="/users/33694723/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
�����Ա
</h2>
</a>
<div class="articleGender manIcon">44</div>
</div>

<a href="/article/119750485" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


�����磬���Ŵ󺰣������Ϲ��ۼҵĹ�©�ˣ�<br/>�£���˵�����ϱ�Թ�������յ��������׷���<br/>ԭ����������ˮ�ٰ���

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">2296</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119750485" data-share="/article/119750485" id="c-119750485" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">13</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119750485" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119750485" class="up">
<a href="javascript:voting(119750485,1)" class="voting" data-article="119750485" id="up-119750485" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2327</span>
</a>
</li>
<li id="vote-dn-119750485" class="down">
<a href="javascript:voting(119750485,-1)" class="voting" data-article="119750485" id="dn-119750485" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-31</span>
</a>
</li>
<li class="comments">
<a href="/article/119750485" id="c-119750485" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119750485" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">��ɽδ�Ϻ��վɣ�</span>
<div class="main-text">
©������ˮ������¥�����Դ�������
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


11

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809241'>


<div class="author clearfix">
<a href="/users/12433067/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1243/12433067/thumb/20170608174016.JPEG?imageView2/1/w/90/h/90" alt="���һ˦�����ĺ�">
</a>
<a href="/users/12433067/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
���һ˦�����ĺ�
</h2>
</a>
<div class="articleGender manIcon">30</div>
</div>

<a href="/article/118809241" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


���²���������á�¥����Ӫһ��С���ݣ������Ǽ���ꡣ���Ǳ���������������ӹ�ȥ�棬���������ϰ���ϴ�롣���ʵ�:���壬��ô������ϴ��ѽ��������ô��ϴ��˲��о������ϰ��ܵ���10000����ʵ�˺���

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">746</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/118809241" data-share="/article/118809241" id="c-118809241" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">2</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_118809241" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809241" class="up">
<a href="javascript:voting(118809241,1)" class="voting" data-article="118809241" id="up-118809241" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">769</span>
</a>
</li>
<li id="vote-dn-118809241" class="down">
<a href="javascript:voting(118809241,-1)" class="voting" data-article="118809241" id="dn-118809241" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-23</span>
</a>
</li>
<li class="comments">
<a href="/article/118809241" id="c-118809241" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119759386'>


<div class="author clearfix">
<a href="/users/33373264/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3337/33373264/thumb/20171004220626.JPEG?imageView2/1/w/90/h/90" alt="����baby">
</a>
<a href="/users/33373264/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
����baby
</h2>
</a>
<div class="articleGender womenIcon">18</div>
</div>

<a href="/article/119759386" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


���Դ�����

</span>

</div>
</a>
<!-- ͼƬ��gif -->



<div class="thumb">

<a href="/article/119759386" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11975/119759386/medium/app119759386.jpg" alt="����#119759386" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">1329</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119759386" data-share="/article/119759386" id="c-119759386" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">10</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119759386" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119759386" class="up">
<a href="javascript:voting(119759386,1)" class="voting" data-article="119759386" id="up-119759386" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1364</span>
</a>
</li>
<li id="vote-dn-119759386" class="down">
<a href="javascript:voting(119759386,-1)" class="voting" data-article="119759386" id="dn-119759386" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-35</span>
</a>
</li>
<li class="comments">
<a href="/article/119759386" id="c-119759386" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119759386" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">WAJJһЦ������</span>
<div class="main-text">
�ָ�������
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


6

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119764743'>


<div class="author clearfix">
<a href="/users/10904125/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1090/10904125/thumb/20140711122500.jpg?imageView2/1/w/90/h/90" alt="�����Կ���">
</a>
<a href="/users/10904125/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
�����Կ���
</h2>
</a>
<div class="articleGender manIcon">23</div>
</div>

<a href="/article/119764743" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


����23�����գ����Լ����Ը�ɡ������5000�޾�ȥ�㶫��ǰŮ�Ѻ�������һ��ӻ�����14����ֵġ������������ˣ�������һֱ����  �������

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">1810</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119764743" data-share="/article/119764743" id="c-119764743" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">46</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119764743" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119764743" class="up">
<a href="javascript:voting(119764743,1)" class="voting" data-article="119764743" id="up-119764743" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1873</span>
</a>
</li>
<li id="vote-dn-119764743" class="down">
<a href="javascript:voting(119764743,-1)" class="voting" data-article="119764743" id="dn-119764743" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-63</span>
</a>
</li>
<li class="comments">
<a href="/article/119764743" id="c-119764743" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119764743" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">ҹ�ܳ������ĺ�������</span>
<div class="main-text">
����ӾͲ��ӣ���5ǧ�ޣ���������ڶ��ӻ����ˡ�һ����ģ��Լ����ﵽ����ô���û�����������
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


24

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119764704'>


<div class="author clearfix">
<a href="/users/25268858/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2526/25268858/thumb/20171103055534.JPEG?imageView2/1/w/90/h/90" alt="С�������">
</a>
<a href="/users/25268858/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
С�������
</h2>
</a>
<div class="articleGender womenIcon">23</div>
</div>

<a href="/article/119764704" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


���ɢ�����Ϲ�������ǰ�棬Ȼ��ͻȻͣ��������׼��������ôͣ����ʱ��ֻ�����۵�һ�������˸���ƨ��Ȼ���������µؼ�����ǰ�ߡ�������

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">900</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119764704" data-share="/article/119764704" id="c-119764704" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">9</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119764704" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119764704" class="up">
<a href="javascript:voting(119764704,1)" class="voting" data-article="119764704" id="up-119764704" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">912</span>
</a>
</li>
<li id="vote-dn-119764704" class="down">
<a href="javascript:voting(119764704,-1)" class="voting" data-article="119764704" id="dn-119764704" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-12</span>
</a>
</li>
<li class="comments">
<a href="/article/119764704" id="c-119764704" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119764906'>


<div class="author clearfix">
<a href="/users/34246786/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3424/34246786/thumb/20171101204316.JPEG?imageView2/1/w/90/h/90" alt="�����š���">
</a>
<a href="/users/34246786/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
�����š���
</h2>
</a>
<div class="articleGender womenIcon">12</div>
</div>

<a href="/article/119764906" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


һ������İְְѶ��ӷ��ڲ����Ϲ��̳����̳�ͻȻ�����˽���к�ǿ�����֣����Ӿ�ץ�Űְֵ�ͷ����������Ť��С��壬��ץͷ���İְ�һ������ʹ�������͵��ζ����趯ͷ����

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">1101</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119764906" data-share="/article/119764906" id="c-119764906" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">13</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119764906" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119764906" class="up">
<a href="javascript:voting(119764906,1)" class="voting" data-article="119764906" id="up-119764906" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1118</span>
</a>
</li>
<li id="vote-dn-119764906" class="down">
<a href="javascript:voting(119764906,-1)" class="voting" data-article="119764906" id="dn-119764906" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/119764906" id="c-119764906" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809005'>


<div class="author clearfix">
<a href="/users/30016699/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3001/30016699/thumb/20170331001525.JPEG?imageView2/1/w/90/h/90" alt="SnЦ����">
</a>
<a href="/users/30016699/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
SnЦ����
</h2>
</a>
<div class="articleGender manIcon">24</div>
</div>

<a href="/article/118809005" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


��ľ�л���а��Сʱ��ĸо��أ�

</span>

</div>
</a>
<!-- ͼƬ��gif -->



<div class="thumb">

<a href="/article/118809005" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11880/118809005/medium/app118809005.jpg" alt="����#118809005" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">552</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/118809005" data-share="/article/118809005" id="c-118809005" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">6</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_118809005" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809005" class="up">
<a href="javascript:voting(118809005,1)" class="voting" data-article="118809005" id="up-118809005" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">566</span>
</a>
</li>
<li id="vote-dn-118809005" class="down">
<a href="javascript:voting(118809005,-1)" class="voting" data-article="118809005" id="dn-118809005" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-14</span>
</a>
</li>
<li class="comments">
<a href="/article/118809005" id="c-118809005" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119765072'>


<div class="author clearfix">
<a href="/users/23331917/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2333/23331917/thumb/2017111618530749.JPEG?imageView2/1/w/90/h/90" alt="36D��ɵ���">
</a>
<a href="/users/23331917/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
36D��ɵ���
</h2>
</a>
<div class="articleGender womenIcon">25</div>
</div>

<a href="/article/119765072" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


�����������ͬ�£��Ͻ����ĵ�:�Ҵ�����ԭ���Ұɣ�<br/>��ͬ�º�����˵:ԭ������ԣ�����������˯һ����<br/>��ʱ�Դ�һ��˵��:�������ֺ��£���<br/>�鵰�������Ƕ������������Ұ�����

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">895</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119765072" data-share="/article/119765072" id="c-119765072" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">41</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119765072" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119765072" class="up">
<a href="javascript:voting(119765072,1)" class="voting" data-article="119765072" id="up-119765072" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">912</span>
</a>
</li>
<li id="vote-dn-119765072" class="down">
<a href="javascript:voting(119765072,-1)" class="voting" data-article="119765072" id="dn-119765072" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/119765072" id="c-119765072" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119765072" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">���ݮ��</span>
<div class="main-text">
��ͬ�¼����������״Σ����������С����������֡����������ֺ���?��
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


23

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762249'>


<div class="author clearfix">
<a href="/users/20115333/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2011/20115333/thumb/2017111200131222.JPEG?imageView2/1/w/90/h/90" alt="����Ӣ��Сľ��">
</a>
<a href="/users/20115333/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
����Ӣ��Сľ��
</h2>
</a>
<div class="articleGender womenIcon">68</div>
</div>

<a href="/article/119762249" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


��ĩ�Ұ���˵���ҳԴ�͡���һ�ϣ������̿���������ģʽ���Ұֻ������ܣ��������˿������ɵ���������˵:��������Ƶĳ��ඪ���Һ�����һ������������:ʲô���Ұ�:������

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">1177</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119762249" data-share="/article/119762249" id="c-119762249" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">14</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119762249" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762249" class="up">
<a href="javascript:voting(119762249,1)" class="voting" data-article="119762249" id="up-119762249" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1194</span>
</a>
</li>
<li id="vote-dn-119762249" class="down">
<a href="javascript:voting(119762249,-1)" class="voting" data-article="119762249" id="dn-119762249" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/119762249" id="c-119762249" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119762249" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">���㣺</span>
<div class="main-text">
������ӷ��£��Ǹ����ܳԣ���������[����]
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


7

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119745840'>


<div class="author clearfix">
<a href="/users/31017736/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3101/31017736/thumb/20160124002717.jpg?imageView2/1/w/90/h/90" alt="918���Ӣ��">
</a>
<a href="/users/31017736/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
918���Ӣ��
</h2>
</a>
<div class="articleGender womenIcon">36</div>
</div>

<a href="/article/119745840" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


��λ���ѣ��������Ѫ�ˣ�ǧ��Ҫ���Ų�Ҫ����Ϊʲô��������ǻ���ǰ����̵�Ѫ��ȥ��������һ���Ѫ�����Ұ��ŵô���˯��ץ��Կ������ұ����ߡ����û��������û����������������

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">3630</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119745840" data-share="/article/119745840" id="c-119745840" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">66</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119745840" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119745840" class="up">
<a href="javascript:voting(119745840,1)" class="voting" data-article="119745840" id="up-119745840" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3673</span>
</a>
</li>
<li id="vote-dn-119745840" class="down">
<a href="javascript:voting(119745840,-1)" class="voting" data-article="119745840" id="dn-119745840" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-43</span>
</a>
</li>
<li class="comments">
<a href="/article/119745840" id="c-119745840" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762767'>


<div class="author clearfix">
<a href="/users/22085995/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2208/22085995/thumb/2017111622015739.JPEG?imageView2/1/w/90/h/90" alt="�����ԣ���İ���">
</a>
<a href="/users/22085995/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
�����ԣ���İ���
</h2>
</a>
<div class="articleGender manIcon">18</div>
</div>

<a href="/article/119762767" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


�����οΣ�������Ϯ��������˼������ȥ<br/>��Ȼ���ֻ����ˣ�˵���£��ô����ϰ<br/>�Ȱ�����һ�ߣ���Ҳ��ȥ��˭֪���������Ŵ��������ˡ���

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">2969</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119762767" data-share="/article/119762767" id="c-119762767" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">34</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119762767" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762767" class="up">
<a href="javascript:voting(119762767,1)" class="voting" data-article="119762767" id="up-119762767" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2997</span>
</a>
</li>
<li id="vote-dn-119762767" class="down">
<a href="javascript:voting(119762767,-1)" class="voting" data-article="119762767" id="dn-119762767" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-28</span>
</a>
</li>
<li class="comments">
<a href="/article/119762767" id="c-119762767" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119762767" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">���㣺</span>
<div class="main-text">
���ɵĻ���˵���ܶ���ס����ϡ��զ����[����]
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


35

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809922'>


<div class="author clearfix">
<a href="/users/26728684/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2672/26728684/thumb/20150318174320.jpg?imageView2/1/w/90/h/90" alt="ʲô����ûע���">
</a>
<a href="/users/26728684/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
ʲô����ûע���
</h2>
</a>
<div class="articleGender manIcon">32</div>
</div>

<a href="/article/118809922" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


�����´��꣬��ͬ������Ͳ�Ҷ��Լ�����С���ſڵȣ��쵽��ʱ���������������<br/>��˵��ȫ���ſڵ�<br/>��æ˵������ô���꣬����ȫ������<br/>��˵��ȫ���Ǳ�����<br/>�ң�������������

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">3727</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/118809922" data-share="/article/118809922" id="c-118809922" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">26</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_118809922" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809922" class="up">
<a href="javascript:voting(118809922,1)" class="voting" data-article="118809922" id="up-118809922" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3801</span>
</a>
</li>
<li id="vote-dn-118809922" class="down">
<a href="javascript:voting(118809922,-1)" class="voting" data-article="118809922" id="dn-118809922" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-74</span>
</a>
</li>
<li class="comments">
<a href="/article/118809922" id="c-118809922" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119763193'>


<div class="author clearfix">
<a href="/users/33922427/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3392/33922427/thumb/20170622234817.JPEG?imageView2/1/w/90/h/90" alt="����9">
</a>
<a href="/users/33922427/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
����9
</h2>
</a>
<div class="articleGender manIcon">0</div>
</div>

<a href="/article/119763193" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


˭�й������ľ�����ȥ�����֤��ʱ�����ֱ�������ͬ�����֣���֮ǰ��ҵ֤�ϵ����ֲ�һ���ˡ��ң��Ҹ��ף���ĸ�����֤�ϵ����ֶ���д���ˣ��Ӵ˽���ʹ��ˣ�ֻ����ʱ����»���ȥ��λ��֤����֤����������ĳĳĳ��

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">816</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119763193" data-share="/article/119763193" id="c-119763193" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">17</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119763193" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119763193" class="up">
<a href="javascript:voting(119763193,1)" class="voting" data-article="119763193" id="up-119763193" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">827</span>
</a>
</li>
<li id="vote-dn-119763193" class="down">
<a href="javascript:voting(119763193,-1)" class="voting" data-article="119763193" id="dn-119763193" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-11</span>
</a>
</li>
<li class="comments">
<a href="/article/119763193" id="c-119763193" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762101'>


<div class="author clearfix">
<a href="/users/33694723/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3369/33694723/thumb/20171110211954.JPEG?imageView2/1/w/90/h/90" alt="�����Ա">
</a>
<a href="/users/33694723/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
�����Ա
</h2>
</a>
<div class="articleGender manIcon">44</div>
</div>

<a href="/article/119762101" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


Сʱ������˵����Ϧ���������ﺬ���eʺ���ӣ����������Ӳ�԰���ҹ���˾���������ţ��֯Ů��˵������<br/>��ʱ����������Ů˵�����Ҿ������ˣ����ڲ�԰��Ȱ��ȣ����˯���ˡ�<br/>����ʱ�����������e��ĭ�ӣ�һ����ã�ز�����ؼ��ˣ�<br/>�����˲�֪���Ǻ�С���ӵģ�

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">1794</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119762101" data-share="/article/119762101" id="c-119762101" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">35</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119762101" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762101" class="up">
<a href="javascript:voting(119762101,1)" class="voting" data-article="119762101" id="up-119762101" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1815</span>
</a>
</li>
<li id="vote-dn-119762101" class="down">
<a href="javascript:voting(119762101,-1)" class="voting" data-article="119762101" id="dn-119762101" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-21</span>
</a>
</li>
<li class="comments">
<a href="/article/119762101" id="c-119762101" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119763035'>


<div class="author clearfix">
<span style="height: 35px">
<img src="//static.qiushibaike.com/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87" alt="�����û�">
</span>
<span>
<h2>�����û�</h2>
</span>
<!-- <div class="articleGender manIcon">32</div> -->
</div>

<a href="/article/119763035" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


ȷʵ������������Ƕ�������ģ�

</span>

</div>
</a>
<!-- ͼƬ��gif -->



<div class="thumb">

<a href="/article/119763035" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11976/119763035/medium/app119763035.jpg" alt="����#119763035" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">1425</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119763035" data-share="/article/119763035" id="c-119763035" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">48</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119763035" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119763035" class="up">
<a href="javascript:voting(119763035,1)" class="voting" data-article="119763035" id="up-119763035" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1476</span>
</a>
</li>
<li id="vote-dn-119763035" class="down">
<a href="javascript:voting(119763035,-1)" class="voting" data-article="119763035" id="dn-119763035" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-51</span>
</a>
</li>
<li class="comments">
<a href="/article/119763035" id="c-119763035" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119763035" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">û��ô��6j��</span>
<div class="main-text">
�ظ� 14¥�����Ǻ��ϵģ��һ�����
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


7

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762112'>


<div class="author clearfix">
<a href="/users/31557645/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3155/31557645/thumb/201711171208508.JPEG?imageView2/1/w/90/h/90" alt="�һ����Ķ�Са">
</a>
<a href="/users/31557645/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
�һ����Ķ�Са
</h2>
</a>
<div class="articleGender manIcon">26</div>
</div>

<a href="/article/119762112" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


��ѧ�ϿΣ�������ʦҪ�����ҵ��С��ûд���������������ض���ʦ˵������ʦ������ҵ�������ˣ������ſ����������ѡ���˵��ָ��ָС�ڡ�<br/>С������ͷ������ʦ����һ���ֶ�ûд����

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">7958</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119762112" data-share="/article/119762112" id="c-119762112" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">69</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119762112" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762112" class="up">
<a href="javascript:voting(119762112,1)" class="voting" data-article="119762112" id="up-119762112" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">8021</span>
</a>
</li>
<li id="vote-dn-119762112" class="down">
<a href="javascript:voting(119762112,-1)" class="voting" data-article="119762112" id="dn-119762112" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-63</span>
</a>
</li>
<li class="comments">
<a href="/article/119762112" id="c-119762112" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119762112" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">��ؼ�棺</span>
<div class="main-text">
������һ���Ķ���  ������һ����
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


65

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809712'>


<div class="author clearfix">
<a href="/users/32062099/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3206/32062099/thumb/20160628155848.jpg?imageView2/1/w/90/h/90" alt="�Ҹ���̨">
</a>
<a href="/users/32062099/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
�Ҹ���̨
</h2>
</a>
<div class="articleGender manIcon">34</div>
</div>

<a href="/article/118809712" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


�������������˲���̫�࣬˳�ֽ��㽶������ߵ���λ�ϣ���һվ����һ���ӣ�ֻ���ſ��ֻ���Ҳûע��������ҵ��㽶���ˣ����ż�����һ����С���ҵ��㽶Ҫ���ˣ���������һ�������������ۣ���ô��ôӲ������ûʲô�������Ա�һƯ�����ȴ������ԿԵ�Ц���������㲻����

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">3849</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/118809712" data-share="/article/118809712" id="c-118809712" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">37</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_118809712" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809712" class="up">
<a href="javascript:voting(118809712,1)" class="voting" data-article="118809712" id="up-118809712" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3920</span>
</a>
</li>
<li id="vote-dn-118809712" class="down">
<a href="javascript:voting(118809712,-1)" class="voting" data-article="118809712" id="dn-118809712" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-71</span>
</a>
</li>
<li class="comments">
<a href="/article/118809712" id="c-118809712" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/118809712" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">�ෲ�ˡ�oO��</span>
<div class="main-text">
����㽶�����ŷŵ�������������ŷţ���ô���ۣ�
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


20

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762342'>


<div class="author clearfix">
<a href="/users/33807867/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3380/33807867/thumb/20171120010403.JPEG?imageView2/1/w/90/h/90" alt="��ζ�̷�">
</a>
<a href="/users/33807867/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
��ζ�̷�
</h2>
</a>
<div class="articleGender manIcon">25</div>
</div>

<a href="/article/119762342" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


�ս��ʱ�����ų��ܣ����ļ�����ˤ�˵��ӣ����û��һ���ӣ����������������¥������������ţ���׼��������˵�������达���Ҷ���Ϳ�ʼ��������:��������Ķ����������ٸ���ˤһ�����ԣ�������Ҳˤ�ˣ�����

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">2902</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119762342" data-share="/article/119762342" id="c-119762342" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">47</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119762342" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762342" class="up">
<a href="javascript:voting(119762342,1)" class="voting" data-article="119762342" id="up-119762342" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2939</span>
</a>
</li>
<li id="vote-dn-119762342" class="down">
<a href="javascript:voting(119762342,-1)" class="voting" data-article="119762342" id="dn-119762342" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-37</span>
</a>
</li>
<li class="comments">
<a href="/article/119762342" id="c-119762342" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119762342" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">����A�Υ���</span>
<div class="main-text">
����ѽ��֪�����Ҹ����Ų����ף���һ�����������ˣ�����Ҳ���������
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


52

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762934'>


<div class="author clearfix">
<a href="/users/3309111/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/330/3309111/thumb/20171117063717.JPEG?imageView2/1/w/90/h/90" alt="������﷦ζ">
</a>
<a href="/users/3309111/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
������﷦ζ
</h2>
</a>
<div class="articleGender manIcon">26</div>
</div>

<a href="/article/119762934" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


������С������·������������ô�ߣ���С�����˴������ۣ��ʣ�����������·ȥ�ػ�������ȥ�أ�������������ȥ���ǵ�Ȼ�������ˣ��� ���ǣ�С����ѻ����Ǯ���ݸ����壺���������Ǻá�������ӹ�Ǯ����С�������̴�У���������ʮ���Ӻ󣬴������Ź����ֵ�Ѻ�ͳ����������뿪���ֳ���

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">1074</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119762934" data-share="/article/119762934" id="c-119762934" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">13</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119762934" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762934" class="up">
<a href="javascript:voting(119762934,1)" class="voting" data-article="119762934" id="up-119762934" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1096</span>
</a>
</li>
<li id="vote-dn-119762934" class="down">
<a href="javascript:voting(119762934,-1)" class="voting" data-article="119762934" id="dn-119762934" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-22</span>
</a>
</li>
<li class="comments">
<a href="/article/119762934" id="c-119762934" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119763245'>


<div class="author clearfix">
<a href="/users/33138205/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3313/33138205/thumb/2016121916032218.JPEG?imageView2/1/w/90/h/90" alt="����ͬЦ��ų�">
</a>
<a href="/users/33138205/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
����ͬЦ��ų�
</h2>
</a>
<div class="articleGender manIcon">22</div>
</div>

<a href="/article/119763245" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


˲��о���˫ʮһ�Ļ���һ��Ҳû��ϵ�ˣ�������[Ц��][Ц��][Ц��]

</span>

</div>
</a>
<!-- ͼƬ��gif -->



<div class="thumb">

<a href="/article/119763245" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11976/119763245/medium/app119763245.jpg" alt="����#119763245" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">2581</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119763245" data-share="/article/119763245" id="c-119763245" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">76</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119763245" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119763245" class="up">
<a href="javascript:voting(119763245,1)" class="voting" data-article="119763245" id="up-119763245" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2610</span>
</a>
</li>
<li id="vote-dn-119763245" class="down">
<a href="javascript:voting(119763245,-1)" class="voting" data-article="119763245" id="dn-119763245" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-29</span>
</a>
</li>
<li class="comments">
<a href="/article/119763245" id="c-119763245" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>


<a href="/article/119763245" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">ҹ����������������</span>
<div class="main-text">
����һ��Ӳ�����뷨����һ�������Ľ��顣����һ��ʪ���յĹ��̣���һ��������Ľ�֡����뱧��������ۺţ��������ð�ţ��׸���ľ�ţ������ҵĸ�̾�ţ��������С���ţ�����������һ��ʡ�Ժ�....
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


40

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762313'>


<div class="author clearfix">
<a href="/users/16807715/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1680/16807715/thumb/20160219231007.jpg?imageView2/1/w/90/h/90" alt="��HUa1">
</a>
<a href="/users/16807715/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
��HUa1
</h2>
</a>
<div class="articleGender manIcon">101</div>
</div>

<a href="/article/119762313" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


��������������

</span>

</div>
</a>
<!-- ͼƬ��gif -->



<div class="thumb">

<a href="/article/119762313" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11976/119762313/medium/app119762313.jpg" alt="����#119762313" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">873</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/119762313" data-share="/article/119762313" id="c-119762313" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">8</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_119762313" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762313" class="up">
<a href="javascript:voting(119762313,1)" class="voting" data-article="119762313" id="up-119762313" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">886</span>
</a>
</li>
<li id="vote-dn-119762313" class="down">
<a href="javascript:voting(119762313,-1)" class="voting" data-article="119762313" id="dn-119762313" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-13</span>
</a>
</li>
<li class="comments">
<a href="/article/119762313" id="c-119762313" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809851'>


<div class="author clearfix">
<a href="/users/28819200/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//static.qiushibaike.com/images/thumb/missing.png?imageView2/1/w/90/h/90" alt="��骡�">
</a>
<a href="/users/28819200/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
��骡�
</h2>
</a>
<div class="articleGender womenIcon">21</div>
</div>

<a href="/article/118809851" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


����һ����Ů����ͦ�ÿ��ģ���������̫�ã��Ҿ�Ȼһֱ���˼�ȥ����������Ȼ��С��ͬ���С���ö�ȥ�������������ģ�������һֱȰ�˼��˼һ᲻����Ϊ����ƭ��

</span>

</div>
</a>
<!-- ͼƬ��gif -->


<div class="stats">
<!-- Ц������������ -->


<span class="stats-vote"><i class="number">366</i> ��Ц</span>
<span class="stats-comments">
<span class="dash"> �� </span>
<a href="/article/118809851" data-share="/article/118809851" id="c-118809851" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">5</i> ����
</a>
</span>
</div>
<div id="qiushi_counts_118809851" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809851" class="up">
<a href="javascript:voting(118809851,1)" class="voting" data-article="118809851" id="up-118809851" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">381</span>
</a>
</li>
<li id="vote-dn-118809851" class="down">
<a href="javascript:voting(118809851,-1)" class="voting" data-article="118809851" id="dn-118809851" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-15</span>
</a>
</li>
<li class="comments">
<a href="/article/118809851" id="c-118809851" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="����΢��" rel="nofollow">΢��</a>
<a class="share-qq" data-type="qq" title="����QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="����QQ�ռ�" rel="nofollow">QQ�ռ�</a>
<a class="share-weibo" data-type="weibo" title="����΢��" rel="nofollow">΢��</a>
</div>
<div class="single-clear"></div>

</div>





<!-- ȫ�ַ�ҳ��� -->

<ul class="pagination">


<li>
<span class="current" >
1
</span>
</li>




<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="page-numbers">
2
</span>
</a>
</li>



<li>
<a href="/hot/page/3/" rel="nofollow">
<!--<a href="/hot/page/3/" rel="nofollow">-->
<span class="page-numbers">
3
</span>
</a>
</li>



<li>
<a href="/hot/page/4/" rel="nofollow">
<!--<a href="/hot/page/4/" rel="nofollow">-->
<span class="page-numbers">
4
</span>
</a>
</li>



<li>
<a href="/hot/page/5/" rel="nofollow">
<!--<a href="/hot/page/5/" rel="nofollow">-->
<span class="page-numbers">
5
</span>
</a>
</li>



<li>
<span class="dots">
��
</span>
</li>


<li>
<a href="/hot/page/13/" rel="nofollow">
<!--<a href="/hot/page/13/" rel="nofollow">-->
<span class="page-numbers">
13
</span>
</a>
</li>


<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="next">
��һҳ
</span>
</a>
</li>

</ul>


</div>



<div class="col2">
<div id="sidebar" class="sidebar">

<div class="shopwindow">
<!-- 55736473��web-�Ҳ�����-up ���ͣ��̶� �ߴ磺300x250-->
<!-- �¹����룺2017-05-03 -->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29674533"></a>');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29674533";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29674533";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- <script type="text/javascript">
var cpro_id = "u693365";
</script>
<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"></script> -->
</div>

<div class="shopwindow" id="listAd2">
<!-- 55736473��web-�Ҳ�����-up ���ͣ��̶� �ߴ磺300x250-->
<!-- �¹����룺2017-05-03 -->
<script type="text/javascript">
/*�Ҳ�2*/
// var cpro_id = "u693365";
// document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
// 2017-5-23 �޸�
// FTAPI_slotid = 1026761;FTAPI_sync = true
// document.write('<script src="//pic.fastapi.net/sdk/js/a.js" charset="utf-8"><\/script>')
</script>
</div>


<div class="sidebar-other">
<img src="/static/images/productlist/ctrl_d.png">
<p>�����°ٿƼ����ղؼ�</p>
</div>
<div class="sidebar-hot clearfix" id="sidebar-qrcode">
<div class="float-left qrcode">
<img src="/static/images/web_v3/sidebar/qiubai_qrcode.png" alt="���°ٿ� APP ���ض�ά��">
</div>
<div class="float-left btn-box">
<a href="javascript:void(0)" class="btn-download ios" onclick="window.open('https://itunes.apple.com/cn/app/id422853458?mt=8')" target="_blank">iOS ����</a>
<a href="javascript:void(0)" class="btn-download android" onclick="window.open('http://static.qiushibaike.com/qiushibaike.apk')" target="_blank">Android ����</a>
<p class="tips">ɨ���������°ٿ�app</p>
</div>
</div>
<div class="sidebar-hot clearfix">
<h3>��Ц���¾�ѡ</h3>
<ul>

<li class="item">
<a href="/article/119755889" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11975/119755889/medium/app119755889.jpg?imageView2/1/w/146/h/146" alt="��������������"/></span>
</a>
<a href="/article/119755889" title="��������������" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>��������������</p>
</a>
</li>

<li class="item">
<a href="/article/119737657" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11973/119737657/medium/app119737657.jpg?imageView2/1/w/146/h/146" alt="�������Ĳ�"/></span>
</a>
<a href="/article/119737657" title="�������Ĳ�" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>�������Ĳ�</p>
</a>
</li>

<li class="item">
<a href="/article/119674095" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11967/119674095/medium/app119674095.jpg?imageView2/1/w/146/h/146" alt="�¹��ٸ��������������ʲ�"/></span>
</a>
<a href="/article/119674095" title="�¹��ٸ��������������ʲ�" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>�¹��ٸ��������������ʲ�</p>
</a>
</li>

<li class="item">
<a href="/article/119749017" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11974/119749017/medium/app119749017.jpg?imageView2/1/w/146/h/146" alt="�չ������"/></span>
</a>
<a href="/article/119749017" title="�չ������" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>�չ������</p>
</a>
</li>

<li class="item">
<a href="/article/119688081" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11968/119688081/medium/app119688081.jpg?imageView2/1/w/146/h/146" alt="��˳�糵�˿��͵��������յ�"/></span>
</a>
<a href="/article/119688081" title="��˳�糵�˿��͵��������յ�" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>��˳�糵�˿��͵��������յ�</p>
</a>
</li>

<li class="item">
<a href="/article/119696261" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11969/119696261/medium/app119696261.jpg?imageView2/1/w/146/h/146" alt="�����ϰ�˵��Ƥ�����Ļ����ȵ�"/></span>
</a>
<a href="/article/119696261" title="�����ϰ�˵��Ƥ�����Ļ����ȵ�" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>�����ϰ�˵��Ƥ�����Ļ����ȵ�</p>
</a>
</li>

<li class="item">
<a href="/article/119686167" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11968/119686167/medium/app119686167.jpg?imageView2/1/w/146/h/146" alt="����ȱ����"/></span>
</a>
<a href="/article/119686167" title="����ȱ����" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>����ȱ����</p>
</a>
</li>

<li class="item">
<a href="/article/119752549" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="?imageView2/1/w/146/h/146" alt="ϣ����Ҷ���¥�ÿ�ݱ����˼ҵ�̫��"/></span>
</a>
<a href="/article/119752549" title="ϣ����Ҷ���¥�ÿ�ݱ����˼ҵ�̫��" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>ϣ����Ҷ���¥�ÿ�ݱ����˼ҵ�̫��</p>
</a>
</li>

</ul>
</div>
<div class="sidebar-hot clearfix" id="sidebar-tab">
<div class="tab-head">
<h3 class="active" data-type="0">����</h3>
<h3 data-type="1">����</h3>
<h3 data-type="2">ר��</h3>
<h3 data-type="3">�Ƽ�</h3>
</div>
<div class="sidebar-tag-block tab-content0">


<li><i># </i><a href="/joke/2466920/">�����㰮��������</a><i> #</i></li>

<li><i># </i><a href="/joke/2466789/">��Ҫ������Ѷ�����Һ��������</a><i> #</i></li>

<li><i># </i><a href="/joke/2464460/">��Ư�����������湫��</a><i> #</i></li>

<li><i># </i><a href="/joke/2463866/">���������Ҫ��Сѧ˵�θ�</a><i> #</i></li>

<li><i># </i><a href="/joke/2460081/">����ֱ���ͷ�</a><i> #</i></li>

<li><i># </i><a href="/joke/2461644/">�쵼Ҫ��ÿ��д�����嵥</a><i> #</i></li>

<li><i># </i><a href="/joke/2461961/">���볤��,�赸</a><i> #</i></li>

<li><i># </i><a href="/joke/2464931/">�����Ҫ������Աlily</a><i> #</i></li>

<li><i># </i><a href="/joke/2463876/">�����Ҫ��Сѧ���˼</a><i> #</i></li>

<li><i># </i><a href="/joke/2459638/">��ҪͶ����ˮ��</a><i> #</i></li>


</div>
<div class="sidebar-tag-block tab-content1 hide">


<li><i># </i><a href="/joke/2467574/">�Ұ�����������Ϫ</a><i> #</i></li>

<li><i># </i><a href="/joke/2467573/">�Ұ��������������Ϊ</a><i> #</i></li>

<li><i># </i><a href="/joke/2467572/">�Ұ�����һ��ֲ��</a><i> #</i></li>

<li><i># </i><a href="/joke/2467571/">�Ұ�����Ĵ���ֲ��԰</a><i> #</i></li>

<li><i># </i><a href="/joke/2467570/">�Ұ�����Ĵ�ɽӦ����ôд</a><i> #</i></li>

<li><i># </i><a href="/joke/2467569/">���������Ұ�����</a><i> #</i></li>

<li><i># </i><a href="/joke/2467568/">�Ұ����������ֹ���Ʒ</a><i> #</i></li>

<li><i># </i><a href="/joke/2467567/">�Ұ������ֹ�չ</a><i> #</i></li>

<li><i># </i><a href="/joke/2467566/">�Ұ�������ܲ���</a><i> #</i></li>

<li><i># </i><a href="/joke/2467565/">���Ұ�����ˮ��</a><i> #</i></li>


</div>
<div class="sidebar-tag-block tab-content2 hide">


<li><i># </i><a href="/key/4682977/">�㶫��+��</a><i> #</i></li>

<li><i># </i><a href="/key/4683739/">����Ҫ��˵�����Ķ�</a><i> #</i></li>

<li><i># </i><a href="/key/4702769/">�ҵĺ������赸��ȫ</a><i> #</i></li>

<li><i># </i><a href="/key/4677850/">��˵�ص�Ӣ��</a><i> #</i></li>

<li><i># </i><a href="/key/4679549/">����,�������˵,�ܼ�.</a><i> #</i></li>

<li><i># </i><a href="/key/4700169/">�����ֻ���ʲô�����</a><i> #</i></li>

<li><i># </i><a href="/key/4690877/">�й���������������</a><i> #</i></li>

<li><i># </i><a href="/key/4681939/">������������˵�İ���</a><i> #</i></li>

<li><i># </i><a href="/key/4689878/">�й����������幢˹��</a><i> #</i></li>

<li><i># </i><a href="/key/4689001/">�й���������Ļ̫��</a><i> #</i></li>


</div>
<div class="sidebar-tag-block tab-content3 hide">


<li><i># </i><a href="/key/4705199/">�й����赸���һ�����������</a><i> #</i></li>

<li><i># </i><a href="/key/4705198/">�й����赸ʷ������������</a><i> #</i></li>

<li><i># </i><a href="/key/4705197/">�й����赸���Ĳ���������</a><i> #</i></li>

<li><i># </i><a href="/key/4705196/">�й����赸��ʮ�ڱ�������</a><i> #</i></li>

<li><i># </i><a href="/key/4705195/">�й����赸��Ʒ���б�������</a><i> #</i></li>

<li><i># </i><a href="/key/4705194/">�й����赸���������</a><i> #</i></li>

<li><i># </i><a href="/key/4705193/">�й����赸�ź��ձ�������</a><i> #</i></li>

<li><i># </i><a href="/key/4705192/">�й����赸��������������</a><i> #</i></li>

<li><i># </i><a href="/key/4705191/">�й����赸����ɱ�������</a><i> #</i></li>

<li><i># </i><a href="/key/4705190/">�й����赸������ʱ�������</a><i> #</i></li>


</div>
</div>

<div class="shopwindow" id="listAd3">
<!-- 55736473��web-�Ҳ�����-up ���ͣ��̶� �ߴ磺300x250-->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29640993"></a >');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29640993";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29640993";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- �¹����룺2017-05-03 -->
<!-- <script>
var cpro_id = "u1101312";
document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
</script> -->
</div>

<div class="shopwindow">
<!-- 2017.10.16 ע�� -->
<!-- <script type="text/javascript" src="https://s.haiyunimg.com/SSP/30169.js"></script> -->
<!-- 2017.10.16 ��� -->
<script>
var mediav_ad_pub = 'klT513_2129270';
var mediav_ad_width = '300';
var mediav_ad_height = '250';
</script>
<script type="text/javascript" language="javascript" charset="utf-8" src="//static.mediav.com/js/mvf_g2.js"></script>
</div>

</div>
</div>



</div>
</div>


<div class="foot">

<div class="foot-nav clearfix">
<div class="foot-nav-col">
<h3>
����
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#team" target="_blank" rel="nofollow">
�����ܰ�
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#tech" target="_blank" rel="nofollow">
��������
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#contact" target="_blank" rel="nofollow">
��ϵ��ʽ
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
����
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/feedback.html" target="_blank" rel="nofollow">
���߷���
</a>
</li>
<li>
<a href="//about.qiushibaike.com/agreement.html" target="_blank" rel="nofollow">
�û�Э��
</a>
</li>
<li>
<a href="//about.qiushibaike.com/policy.html" target="_blank" rel="nofollow">
��˽����
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
����
</h3>
<ul>
<li>
<a href="http://android.myapp.com/android/appdetail.jsp?appid=107431&icfa=15144196000105020000&lmid=2031"
target="_blank" rel="external nofollow">
Android �ͻ���
</a>
</li>
<li>
<a href="http://itunes.apple.com/app/id422853458" target="_blank" rel="external nofollow">
iPhone �ͻ���
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
��ע
</h3>
<ul>
<li>
<a href="#" class="foot-wechat">
΢��
<div class="foot-wechat-tips">
<span class="foot-wechat-icon"></span>
�ֻ�ɨ���ά���ע
</div>
</a>
</li>
<li>
<a href="http://weibo.com/qiushibaike" target="_blank" rel="external nofollow">
����΢��
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058" target="_blank" rel="external nofollow">
QQ�ռ�
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
��֯
</h3>
<ul>
<li>
<a href="http://shang.qq.com/wpa/qunwpa?idkey=da34d190ca97a0b21d64ebc6f3ab72c076ed35820e629b78fcf9f6a78f7063cd"
target="_blank" rel="external nofollow">
��վ����Ⱥ
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058/blog/1408597608" target="_blank"
rel="external nofollow">
�ٷ���˿Ⱥ
</a>
</li>
</ul>
</div>
</div>
<div class="foot-copyrights">
<!-- <p>&copy; Qiushibaike.com ���°ٿư�Ȩ����</p>
<p>
<span>��ICP��14028348��-1</span>
<span>��ICP֤140448��</span>
<span>������[2017]2369-247��</span>
<span>
<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />����������11010502031601��</a>
</span>
</p>
<p style="margin-top:8px">�Ѽ����ޣ��������Ƽ����޹�˾</p>
<p style="margin-top:8px">
<span>������Υ���Ͳ�����Ϣ�ٱ��绰��010-84872896</span>
<span>���䣺kefu@qiushibaike.com</span>
</p> -->
<p>������ICP��������ICP��14028348��-1</p>
<p>
<span>�㲥���ӽ�Ŀ������Ӫ���֤���������ֵ�08319��</span>
<span>�����Ļ���Ӫ���֤��������[2017]2369-247��</span>
</p>
<p style="margin-top: 8px">��������Ϣ����ҵ��Ӫ���֤����ICP֤140448��</p>
<p>
<span>�������Ϣ�������������λ������<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />����������11010502031601��</a></span>
</p>
<br>
<p style="margin-top: 8px">�Ѽ����ޣ��������Ƽ����޹�˾</p>
<p>
<span>Υ���Ͳ�����Ϣ�ٱ��绰��010-84872896</span>
<span>���䣺kefu@qiushibaike.com</span>
</p>
<br>
<p style="margin-top: 8px">&copy; Qiushibaike.com ���°ٿư�Ȩ����</p>
</div>
</div>


<div class="signin-box" id="login-form">
<div class="sigin-left">
<div class="signin-account clearfix">
<h4 class="social-signin-heading">�罻�ʺŵ�¼</h4>
<a rel="external nofollow" oauth_href href="https://open.weixin.qq.com/connect/qrconnect?appid=wx559af2d26b56c655&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession%3Fsrc%3Dwx&response_type=code&scope=snsapi_login#wechat_redirect" class="social-btn social-wechat">
ʹ�� ΢�� �˺�</a>
<a rel="external nofollow" oauth_href href="https://api.weibo.com/oauth2/authorize?client_id=63372306&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession" class="social-btn social-weibo">
ʹ�� ΢�� �˺�</a>
<a rel="external nofollow" oauth_href href="https://graph.qq.com/oauth2.0/authorize?which=Login&display=pc&client_id=100251437&response_type=code&redirect_uri=www.qiushibaike.com/new4/session?src=qq" class="social-btn social-qq">
ʹ�� QQ �˺� </a>
</div>
<div class="signin-form clearfix">
<h4 class="social-signin-heading">���°ٿ��˺ŵ�¼</h4>
<form method="post" action="/new4/session">
<input type="hidden" name="_xsrf" value="2|a26d8990|0c5a59f134dd74c4de57f7803ed9cabd|1511145325"/>
<div class="signin-section clearfix">
<input type="text" class="form-input form-input-first" name="login" placeholder="�ǳƻ�����">
<input type="password" class="form-input" name="password" placeholder="����">
<input type="checkbox" id="remember_me" name="remember_me" checked="" value="checked" style="display:none">
</div>
<div class="signin-error" id="signin-error"></div>
<button type="submit" id="form-submit" class="form-submit">��¼</button>
</form>
</div>
<div class="signin-foot clearfix">
<a rel="nofollow" href="/new4/fetchpass" class="fetch-password">��������?</a>
</div>
</div>
</div>

<div class="float-nav">
<a class="float-nav-backtop" href="#" rel="nofollow">
<span class="float-nav-backtop-icon"></span>
</a>
</div>

<!--[if gte IE 6]>
<script type="text/javascript" src="//static.qiushibaike.com/js/src/web/json3.js?v=3a7f66a11a09842cd7555fad039657be"></script>
<![endif]-->
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/libs.min.js?v=bc8ddd36f0e7fed7c27f437c17f23ce0"></script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/app.min.js?v=fb527abdfeb0ca7dcd7ac97d941b61f3"></script>



<script type="text/javascript">
// Google Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-8780108-1', 'auto');
ga('send', 'pageview');
</script>

<script type="text/javascript" async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script type="text/javascript" src="https://cbjs.baidu.com/js/m.js"></script>
<script type="text/javascript">



window.broadJson = '[{&quot;status&quot;: &quot;3&quot;, &quot;code&quot;: &quot;&lt;script&gt;var cpro_id = &#39;u693365&#39;;&lt;/script&gt;&quot;, &quot;name&quot;: &quot;web-sidebar-01&quot;, &quot;count_id&quot;: &quot;&quot;, &quot;url&quot;: &quot;https://cpro.baidustatic.com/cpro/ui/c.js&quot;, &quot;start_time&quot;: &quot;2017-08-31 00:00:00&quot;, &quot;system&quot;: &quot;notlimited&quot;, &quot;site&quot;: &quot;web&quot;, &quot;master&quot;: &quot;�ٶ�����&quot;, &quot;end_time&quot;: &quot;2018-08-28 00:00:00&quot;, &quot;id&quot;: &quot;104&quot;, &quot;position&quot;: &quot;&quot;, &quot;created_at&quot;: &quot;2017-08-31 16:32:10&quot;, &quot;channel&quot;: &quot;&quot;}, {&quot;status&quot;: &quot;3&quot;, &quot;code&quot;: &quot;&lt;script&gt;ADEZ_slotid = 1026761;ADEZ_target=&#39;web-sidebar-02&#39;&lt;/script&gt;&quot;, &quot;name&quot;: &quot;web-sidebar-02&quot;, &quot;count_id&quot;: &quot;&quot;, &quot;url&quot;: &quot;//pic.ggxt.net/sdk/js/core.js&quot;, &quot;start_time&quot;: &quot;2017-08-31 00:00:00&quot;, &quot;system&quot;: &quot;notlimited&quot;, &quot;site&quot;: &quot;web&quot;, &quot;master&quot;: &quot;����&quot;, &quot;end_time&quot;: &quot;2018-09-04 00:00:00&quot;, &quot;id&quot;: &quot;105&quot;, &quot;position&quot;: &quot;&quot;, &quot;created_at&quot;: &quot;2017-08-31 16:33:18&quot;, &quot;channel&quot;: &quot;&quot;}, {&quot;status&quot;: &quot;3&quot;, &quot;code&quot;: &quot;&lt;script&gt;var cpro_id = &#39;u1101312&#39;;&lt;/script&gt;&quot;, &quot;name&quot;: &quot;web-sidebar-03&quot;, &quot;count_id&quot;: &quot;&quot;, &quot;url&quot;: &quot;https://cpro.baidustatic.com/cpro/ui/c.js&quot;, &quot;start_time&quot;: &quot;2018-08-28 00:00:00&quot;, &quot;system&quot;: &quot;notlimited&quot;, &quot;site&quot;: &quot;web&quot;, &quot;master&quot;: &quot;�ٶ�����&quot;, &quot;end_time&quot;: &quot;2018-08-28 00:00:00&quot;, &quot;id&quot;: &quot;106&quot;, &quot;position&quot;: &quot;&quot;, &quot;created_at&quot;: &quot;2017-08-31 17:16:31&quot;, &quot;channel&quot;: &quot;&quot;}, {&quot;status&quot;: &quot;3&quot;, &quot;code&quot;: &quot;&lt;script&gt;&lt;ins class=&#39;adsbygoogle&#39; style=&#39;display:inline-block;width:728px;height:90px&#39; data-ad-client=&#39;ca-pub-7443704194229694&#39; data-ad-slot=&#39;9826878184&#39;&gt;&lt;/ins&gt;&lt;/script&gt;&quot;, &quot;name&quot;: &quot;web-foot&quot;, &quot;count_id&quot;: &quot;&quot;, &quot;url&quot;: &quot;//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js&quot;, &quot;start_time&quot;: &quot;2017-08-31 00:00:00&quot;, &quot;system&quot;: &quot;notlimited&quot;, &quot;site&quot;: &quot;web&quot;, &quot;master&quot;: &quot;�ȸ�&quot;, &quot;end_time&quot;: &quot;2018-08-28 00:00:00&quot;, &quot;id&quot;: &quot;103&quot;, &quot;position&quot;: &quot;&quot;, &quot;created_at&quot;: &quot;2017-08-31 16:29:51&quot;, &quot;channel&quot;: &quot;&quot;}]'
</script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/v3/adsAdmin.min.js?v=9c42f35ae43e17caf141e9d6ebe32cbb"></script>
</body>
</html>

>>> content = response.read().decode('utf-8')
pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0],item[1],item[2],item[3],item[4]
    
>>> content = response.read().decode('utf-8')
>>> pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="st
		     
SyntaxError: EOL while scanning string literal
>>> items = re.findall(pattern,content)
for item in items:
    print item[0],item[1],item[2],item[3],item[4]


Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 're' is not defined
>>> import urllib
>>> import urllib2
>>> import re

>>> page = 1
>>> url = 'http://www.qiushibaike.com/hot/page/' + str(page)
>>> user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
>>> headers = { 'User-Agent' : user_agent }
>>> try:
	request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?cl
			 
  File "<pyshell#30>", line 4
    response = urllib2.urlopen(request)
                                      ^
IndentationError: unindent does not match any outer indentation level
>>> request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    
>>> items = re.findall(pattern,content)

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 'pattern' is not defined
>>> items = re.findall(pattern,content)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 'pattern' is not defined
>>> items = re.findall(pattern,content)
    for item in items:
	    

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 'pattern' is not defined
>>>  items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
	
  File "<pyshell#35>", line 2
    items = re.findall(pattern,content)
    ^
IndentationError: unexpected indent
>>> items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 'pattern' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
