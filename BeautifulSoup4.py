#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018/8/15

from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<!--[if IE 6]><html class="ie lt-ie8"><![endif]-->
<!--[if IE 7]><html class="ie lt-ie8"><![endif]-->
<!--[if IE 8]><html class="ie ie8"><![endif]-->
<!--[if IE 9]><html class="ie ie9"><![endif]-->
<!--[if !IE]><!--> <html> <!--<![endif]-->

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0,user-scalable=no">

  <!-- Start of Baidu Transcode -->
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta name="applicable-device" content="pc,mobile">
  <meta name="MobileOptimized" content="width"/>
  <meta name="HandheldFriendly" content="true"/>
  <meta name="mobile-agent" content="format=html5;url=https://www.jianshu.com/p/d70041eb25d7">
  <!-- End of Baidu Transcode -->

    <meta name="description"  content="如果你有一个很好的想法，为什么不自己动手做一个App来实现它呢。即使你完全没有编程经验也没有关系，通过以下这些精心挑选的教程和资源，你也一定能作出属于自己的iOS App来。（当然如果你暂时还没有一个好的想法或者觉得自己还没做好充足的准备，那也没关系，你可以收藏这篇“资源集合”，技匠会为你持续更新其中的内容，当你准备好的那天，翻出这篇文章，就可以开始实现你的梦想。 ） （补充：如果你由于网络...">

  <meta name="360-site-verification" content="604a14b53c6b871206001285921e81d8" />
  <meta property="wb:webmaster" content="294ec9de89e7fadb" />
  <meta property="qc:admins" content="104102651453316562112116375" />
  <meta property="qc:admins" content="11635613706305617" />
  <meta property="qc:admins" content="1163561616621163056375" />
  <meta name="google-site-verification" content="cV4-qkUJZR6gmFeajx_UyPe47GW9vY6cnCrYtCHYNh4" />
  <meta name="google-site-verification" content="HF7lfF8YEGs1qtCE-kPml8Z469e2RHhGajy6JPVy5XI" />
  <meta http-equiv="mobile-agent" content="format=html5; url=https://www.jianshu.com/p/d70041eb25d7">

  <!-- Apple -->
  <meta name="apple-mobile-web-app-title" content="简书">

    <!--  Meta for Smart App Banner -->
  <meta name="apple-itunes-app" content="app-id=888237539, app-argument=jianshu://notes/3328010">
  <!-- End -->

  <!--  Meta for Twitter Card -->
  <meta content="summary" property="twitter:card">
  <meta content="@jianshucom" property="twitter:site">
  <meta content="iOS开发完全自学资源集合" property="twitter:title">
  <meta content="如果你有一个很好的想法，为什么不自己动手做一个App来实现它呢。即使你完全没有编程经验也没有关系，通过以下这些精心挑选的教程和资源，你也一定能作出属于自己的iOS App来。..." property="twitter:description">
  <meta content="https://www.jianshu.com/p/d70041eb25d7" property="twitter:url">
  <!-- End -->

  <!--  Meta for OpenGraph -->
  <meta property="fb:app_id" content="865829053512461">
  <meta property="og:site_name" content="简书">
  <meta property="og:title" content="iOS开发完全自学资源集合">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://www.jianshu.com/p/d70041eb25d7">
  <meta property="og:description" content="如果你有一个很好的想法，为什么不自己动手做一个App来实现它呢。即使你完全没有编程经验也没有关系，通过以下这些精心挑选的教程和资源，你也一定能作出属于自己的iOS App来。（当然如果你暂时还没...">
  <!-- End -->

  <!--  Meta for Facebook Applinks -->
  <meta property="al:ios:url" content="jianshu://notes/3328010" />
  <meta property="al:ios:app_store_id" content="888237539" />
  <meta property="al:ios:app_name" content="简书" />

  <meta property="al:android:url" content="jianshu://notes/3328010" />
  <meta property="al:android:package" content="com.jianshu.haruki" />
  <meta property="al:android:app_name" content="简书" />
  <!-- End -->


    <title>iOS开发完全自学资源集合 - 简书</title>

  <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="bU/52E3yWAMePnFaRBd7qwHnKAoZ1O0Ye/YWzbwRCnSBAP5SwA0Zz7O2b2QBNAn6t/a9iVm7fFRPV0ZgfxxNuw==" />

  <link rel="stylesheet" media="all" href="//cdn2.jianshu.io/assets/web-2b26d78a4d3c053b7b1c.css" />
  
  <link rel="stylesheet" media="all" href="//cdn2.jianshu.io/assets/web/pages/notes/show/entry-7fb4c1aebb52435f09b0.css" />

  <link href="//cdn2.jianshu.io/assets/favicons/favicon-e743bfb1821442341c3ab15bdbe804f7ad97676bd07a770ccc9483473aa76f06.ico" rel="shortcut icon" type="image/x-icon">
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/57-a6f1f1ee62ace44f6dc2f6a08575abd3c3b163288881c78dd8d75247682a4b27.png" sizes="57x57" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/72-fb9834bcfce738fd7b9c5e31363e79443e09a81a8e931170b58bc815387c1562.png" sizes="72x72" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/76-49d88e539ff2489475d603994988d871219141ecaa0b1a7a9a1914f4fe3182d6.png" sizes="76x76" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/114-24252fe693524ed3a9d0905e49bff3cbd0228f25a320aa09053c2ebb4955de97.png" sizes="114x114" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/120-1bb7371f5e87f93ce780a5f1a05ff1b176828ee0d1d130e768575918a2e05834.png" sizes="120x120" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/152-bf209460fc1c17bfd3e2b84c8e758bc11ca3e570fd411c3bbd84149b97453b99.png" sizes="152x152" />

  <!-- Start of 访问统计 -->
    <script>
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "//hm.baidu.com/hm.js?0c0e9d9b1e7d617b3e6842e85b9fb068";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    })();
  </script>

  <!-- End of 访问统计 -->
</head>

  <body lang="zh-CN" class="reader-black-font">
    <!-- 全局顶部导航栏 -->
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
  <div class="width-limit">
    <!-- 左上方 Logo -->
    <a class="logo" href="/"><img src="//cdn2.jianshu.io/assets/web/nav-logo-4c7bbafe27adc892f3046e6978459bac.png" alt="Nav logo" /></a>

    <!-- 右上角 -->
      <!-- 未登录显示登录/注册/写文章 -->
      <a class="btn write-btn" target="_blank" href="/writer#/">
        <i class="iconfont ic-write"></i>写文章
</a>      <a class="btn sign-up" id="sign_up" href="/sign_up">注册</a>
      <a class="btn log-in" href="/sign_in">登录</a>

    <!-- 如果用户登录，显示下拉菜单 -->

    <div id="view-mode-ctrl">
    </div>
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#menu" aria-expanded="false">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse" id="menu">
        <ul class="nav navbar-nav">
            <li class="tab ">
              <a href="/">
                <span class="menu-text">首页</span><i class="iconfont ic-navigation-discover menu-icon"></i>
</a>            </li>
            <li class="tab ">
              <a id="web-nav-app-download-btn" class="app-download-btn" href="/apps?utm_medium=desktop&amp;utm_source=navbar-apps"><span class="menu-text">下载App</span><i class="iconfont ic-navigation-download menu-icon"></i></a>
            </li>
          <li class="search">
            <form target="_blank" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
              <input type="text" name="q" id="q" value="" autocomplete="off" placeholder="搜索" class="search-input" />
              <a class="search-btn" href="javascript:void(null)"><i class="iconfont ic-search"></i></a>
</form>          </li>
        </ul>
      </div>
    </div>
  </div>
</nav>

    
<div class="note">
    <a target="_blank" href="/apps/redirect?utm_source=side-banner-click" id="web-note-ad-fixed"><span class="close">&times;</span></a>
  <div class="post">
    <div class="article">
        <h1 class="title">iOS开发完全自学资源集合</h1>

        <!-- 作者区域 -->
        <div class="author">
          <a class="avatar" href="/u/3313b20a4e25">
            <img src="//upload.jianshu.io/users/upload_avatars/1399853/1723bf426bd3.png?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96" alt="96" />
</a>          <div class="info">
            <span class="name"><a href="/u/3313b20a4e25">技匠</a></span>
              <img class="badge-icon" data-toggle="tooltip" title="程序员优秀作者" src="//upload.jianshu.io/user_badge/595a1b60-08f6-4beb-998f-2bf55e230555" alt="595a1b60 08f6 4beb 998f 2bf55e230555" />
            <!-- 关注用户按钮 -->
            <div props-data-classes="user-follow-button-header" data-author-follow-button></div>
            <!-- 文章数据信息 -->
            <div class="meta">
              <!-- 如果文章更新时间大于发布时间，那么使用 tooltip 显示更新时间 -->
                <span class="publish-time" data-toggle="tooltip" data-placement="bottom" title="最后编辑于 2017.12.03 03:23">2016.03.27 19:04*</span>
              <span class="wordage">字数 1905</span>
            </div>
          </div>
          <!-- 如果是当前作者，加入编辑按钮 -->
        </div>


        <!-- 文章内容 -->
        <div data-note-content class="show-content">
          <div class="show-content-free">
            <p>如果你有一个很好的想法，为什么不自己动手做一个App来实现它呢。即使你完全没有编程经验也没有关系，通过以下这些精心挑选的教程和资源，你也一定能作出属于自己的iOS App来。（当然如果你暂时还没有一个好的想法或者觉得自己还没做好充足的准备，那也没关系，你可以收藏这篇“资源集合”，<strong>技匠</strong>会为你持续更新其中的内容，当你准备好的那天，翻出这篇文章，就可以开始实现你的梦想。 ）</p>
<p>（<strong>补充：如果你由于网络原因无法浏览以下YouTube视频教程或书籍，也可以关注我的简书或微信账号techmask，稍后我会将资源下载到我的网盘，并分享给需要的读者<sup>_</sup></strong>）</p>
<hr>
<h3><a href="https://link.jianshu.com?t=https://developer.apple.com/swift/blog/?id=16" target="_blank" rel="nofollow">Building Your First Swift App Video</a></h3>
<p>首先当然是来自苹果的官方教程“构建你的第一个Swift App”了。苹果通过一段只有6分钟的短视频，介绍了如何使用Xcode IDE快速地构建出一个使用Swift编写的APP来。这也是你开始学习iOS开发的一个很好的起点。</p>
<div class="image-package">
<div class="image-container" style="max-width: 536px; max-height: 333px;">
<div class="image-container-fill" style="padding-bottom: 62.129999999999995%;"></div>
<div class="image-view" data-width="536" data-height="333"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-5775264bbfc5f9b7.png" data-original-width="536" data-original-height="333" data-original-format="image/png" data-original-filesize="210485"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=https://www.youtube.com/watch?v=t7xUvFs3cPI&amp;list=UUuD-wbMZDn2C2_GwcMqterg" target="_blank" rel="nofollow">Swift for Absolute Beginners（YouTube视频）</a></h3>
<p>这是一套5集YouTube视频教程，通过一些短小的例子介绍了Swift的基本特性和语法，结合playground的使用，能让Swift的初学者在非常生动的环境下有效地学习这门新兴语言。</p>
<div class="image-package">
<div class="image-container" style="max-width: 540px; max-height: 393px;">
<div class="image-container-fill" style="padding-bottom: 72.78%;"></div>
<div class="image-view" data-width="540" data-height="393"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-1e5178e357aef13c.png" data-original-width="540" data-original-height="393" data-original-format="image/png" data-original-filesize="116648"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://codewithchris.com/how-to-make-an-iphone-app" target="_blank" rel="nofollow">How To Make An iPhone App（YouTube视频）</a></h3>
<p>由CodeWithChris发布的一套视频课程（前17节课是免费的），面向的是那些没有Swift以及iOS开发经验的观众。通过这个教程，你能够从零起步，一步一步在XCode中学习使用Swift来开发iOS App。这套教程包含了Swift语言基础，UIKit，Auot Layout，IBOutlet等内容，对于初学者来说，非常有帮助。</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 433px;">
<div class="image-container-fill" style="padding-bottom: 56.16%;"></div>
<div class="image-view" data-width="771" data-height="433"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-9be0de6ca85db8cc.png" data-original-width="771" data-original-height="433" data-original-format="image/png" data-original-filesize="277595"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://www.appcoda.com/swift/" target="_blank" rel="nofollow">Beginning iOS Programming with Swift</a></h3>
<p>Simon（作者）写了很多非常优秀的iOS教程。“Beginning iOS Programming with Swift”是他最新的一套iOS资源集合，包含一本500页的电子书（包含了大量精美的插图和截屏，读起来完全不会觉得枯燥），对应的源代码，大量App模板以及图标等，而且可以获得免费的更新。这套资源能够帮助你开发出一个优秀的iOS APP。</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 465px;">
<div class="image-container-fill" style="padding-bottom: 48.949999999999996%;"></div>
<div class="image-view" data-width="950" data-height="465"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-2b0e28e674865f0b.png" data-original-width="950" data-original-height="465" data-original-format="image/png" data-original-filesize="586863"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=https://developer.apple.com/design/" target="_blank" rel="nofollow">iOS Design Guidelines</a></h3>
<p>Apple的官方设计指南，包含很多讲解基于iOS进行设计的优秀视频，获奖的应用，新的系统字体San Francisco，以及交互界面设计指南等。</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 346px;">
<div class="image-container-fill" style="padding-bottom: 43.63%;"></div>
<div class="image-view" data-width="793" data-height="346"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-1fd86e9d70a4549c.png" data-original-width="793" data-original-height="346" data-original-format="image/png" data-original-filesize="81906"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=https://www.bloc.io/swiftris-build-your-first-ios-game-with-swift" target="_blank" rel="nofollow">Swiftris - Build Your First iOS Game</a></h3>
<p>如果你希望开发的是一个iOS游戏，那么可以参考这篇教程。其中介绍了如何用Swift开发一个2D俄罗斯方块游戏。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 690px; max-height: 355px;">
<div class="image-container-fill" style="padding-bottom: 51.449999999999996%;"></div>
<div class="image-view" data-width="690" data-height="355"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-198b86bb5a7fa1ff.png" data-original-width="690" data-original-height="355" data-original-format="image/png" data-original-filesize="205472"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://omarfouad.com/blog/2014/08/02/getting-started-uikitdynamics-swift/" target="_blank" rel="nofollow">Getting started with UIKit Dynamics in Swift</a></h3>
<p>UIKit是一个基础的UI库，通过它，你能在你的App中实现非常美妙的物理动效。这篇Blog能够带你深入认识UIKit的使用。</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 600px;">
<div class="image-container-fill" style="padding-bottom: 80.0%;"></div>
<div class="image-view" data-width="750" data-height="600"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-8cd44223a7a855d8.gif" data-original-width="750" data-original-height="600" data-original-format="image/gif" data-original-filesize="596655"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://www.appcoda.com/introduction-auto-layout/" target="_blank" rel="nofollow">Introduction to Auto Layout</a></h3>
<p>Auto layout对于每个设计师来说都非常重要，它能帮助你设计出可适应UI，使应用在不同的设备分辨率以及放置位置下能够正确地显示。</p>
<div class="image-package">
<div class="image-container" style="max-width: 600px; max-height: 305px;">
<div class="image-container-fill" style="padding-bottom: 50.83%;"></div>
<div class="image-view" data-width="600" data-height="305"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-4f3d80b7d622acc8.jpg" data-original-width="600" data-original-height="305" data-original-format="image/jpeg" data-original-filesize="27748"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=https://education.github.com/pack" target="_blank" rel="nofollow">Student Developer Pack</a></h3>
<p>这是GitHub提供的一个针对学生的免费软件集合，包含大量出色的软件工具，如果你是一名学生可以向GitHub申请获取。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 690px; max-height: 339px;">
<div class="image-container-fill" style="padding-bottom: 49.13%;"></div>
<div class="image-view" data-width="690" data-height="339"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-bea111eaf16ea614.png" data-original-width="690" data-original-height="339" data-original-format="image/png" data-original-filesize="77677"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://cocoapods.org/" target="_blank" rel="nofollow">CocoaPods</a></h3>
<p>CocoaPods是一个库管理工具，有了它，你可以快速地将已有类库导入到你的项目中使用。这样可以避免你重复发明轮子，让你直接使用那些非常优秀并且经过验证的第三方库。</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 346px;">
<div class="image-container-fill" style="padding-bottom: 43.8%;"></div>
<div class="image-view" data-width="790" data-height="346"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-4ac909fed2752dfe.png" data-original-width="790" data-original-height="346" data-original-format="image/png" data-original-filesize="78799"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://www.swifttoolbox.io/" target="_blank" rel="nofollow">Swift Toolbox</a></h3>
<p>Swift Toolbox是一个由开源社区驱动的网站，包含了大量由社区开发人员贡献并维护的第三方Swift代码库。你可以直接使用在你的项目中。</p>
<div class="image-package">
<div class="image-container" style="max-width: 690px; max-height: 241px;">
<div class="image-container-fill" style="padding-bottom: 34.93%;"></div>
<div class="image-view" data-width="690" data-height="241"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-e09e0a1d37eb2a68.png" data-original-width="690" data-original-height="241" data-original-format="image/png" data-original-filesize="54472"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://alcatraz.io/" target="_blank" rel="nofollow">Alcatraz</a></h3>
<p>Alcatraz是一套带有用户界面的包管理工具。使用它能够非常方便地寻找并在Xcode上自动安装那些插件、模板、CocoaPods库以及色彩主题。对提高Xcode的使用效率非常有帮助。</p>
<div class="image-package">
<div class="image-container" style="max-width: 683px; max-height: 337px;">
<div class="image-container-fill" style="padding-bottom: 49.34%;"></div>
<div class="image-view" data-width="683" data-height="337"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-dd235536b3b424d2.png" data-original-width="683" data-original-height="337" data-original-format="image/png" data-original-filesize="109294"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://realm.io/" target="_blank" rel="nofollow">Realm: mobile-first database</a></h3>
<p>Realm是一个可以在手机上直接运行，而不需要任何服务器的数据库。它对Swift支持得非常好，如果你的App不要求与服务器交互，那么Realm会是一个数据存储的很好选择。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 511px;">
<div class="image-container-fill" style="padding-bottom: 54.89000000000001%;"></div>
<div class="image-view" data-width="931" data-height="511"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-20ece0a32bf928ab.png" data-original-width="931" data-original-height="511" data-original-format="image/png" data-original-filesize="73792"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=https://github.com/facebook/pop" target="_blank" rel="nofollow">Facebook Pop</a></h3>
<p>Facebook Pop是iOS开发中非常有名的动效库，基于它你能非常方便地定义自己的阻尼效果动效。而最有名的<a href="https://link.jianshu.com?t=https://www.facebook.com/paper" target="_blank" rel="nofollow">Facebook Paper</a>应用就是基于Pop实现的。<br>
</p><div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 249px;">
<div class="image-container-fill" style="padding-bottom: 32.68%;"></div>
<div class="image-view" data-width="762" data-height="249"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-6784b8782edc9f33.png" data-original-width="762" data-original-height="249" data-original-format="image/png" data-original-filesize="48550"></div>
</div>
<div class="image-caption"></div>
</div><p></p>
<hr>
<h3><a href="https://link.jianshu.com?t=https://github.com/mengto/spring" target="_blank" rel="nofollow">Spring: iOS Animation Library in Swift</a></h3>
<p>Spring是一另一个出色的动效库，它允许你在XCode的Stroyboard中直接通过配置来实现动效以及原型。在GitHub上获得了2000颗星。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 393px;">
<div class="image-container-fill" style="padding-bottom: 56.230000000000004%;"></div>
<div class="image-view" data-width="1974" data-height="1110"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-ea6b9522718de81a.jpeg" data-original-width="1974" data-original-height="1110" data-original-format="image/jpeg" data-original-filesize="659892"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=https://get.fabric.io/" target="_blank" rel="nofollow">Fabric - Twitter’s Mobile Development Platform</a></h3>
<p>Twitter的移动开发平台，提供了Twitter登录，统计分析，将特定的推文与自己提供的服务 /App 结合并展示出来的功能。对于围绕Twitter而设计的App非常有用。</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 444px;">
<div class="image-container-fill" style="padding-bottom: 55.50000000000001%;"></div>
<div class="image-view" data-width="800" data-height="444"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-d332df30a827d555.png" data-original-width="800" data-original-height="444" data-original-format="image/png" data-original-filesize="45458"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=https://github.com/allenwong/30DaysofSwift" target="_blank" rel="nofollow">30 Days of Swift</a></h3>
<p>一个设计师用一个月时间学习并使用Swift完成了30个IOS小应用，并将它们分享在GitHub上。这些小应用都各不相同，涵盖了Swift开发的各个方面，非常值得学习。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 562px;">
<div class="image-container-fill" style="padding-bottom: 56.2%;"></div>
<div class="image-view" data-width="1000" data-height="562"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-5c373a3a6c02cf3a.png" data-original-width="1000" data-original-height="562" data-original-format="image/png" data-original-filesize="1085813"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=https://github.com/shu223/iOS-9-Sampler" target="_blank" rel="nofollow">iOS 9 Sampler</a></h3>
<p>这个GitHub代码库以一个个小Demo的形式介绍了iOS 9的一些新特性。你可以直接下载代码，并在XCode中运行这些示例。</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 233px;">
<div class="image-container-fill" style="padding-bottom: 28.910000000000004%;"></div>
<div class="image-view" data-width="806" data-height="233"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-3446b8ab045b387a.png" data-original-width="806" data-original-height="233" data-original-format="image/png" data-original-filesize="55496"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://www.thinkandbuild.it/" target="_blank" rel="nofollow">Think and Build iOS Tutorials</a></h3>
<p>这个网站包含了大量高质量的Swift教程。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 616px; max-height: 332px;">
<div class="image-container-fill" style="padding-bottom: 53.900000000000006%;"></div>
<div class="image-view" data-width="616" data-height="332"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-0057d3b07df1a506.png" data-original-width="616" data-original-height="332" data-original-format="image/png" data-original-filesize="23892"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://www.raywenderlich.com/" target="_blank" rel="nofollow">Raywenderlich</a></h3>
<p>Raywenderlich应该是包含iOS教程最多的网站了，其中既有App教程，也有游戏开发教程，适合从初学者到资深开发人员的各层级用户的需要。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 349px;">
<div class="image-container-fill" style="padding-bottom: 41.010000000000005%;"></div>
<div class="image-view" data-width="851" data-height="349"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-cea87215cb4a6b20.png" data-original-width="851" data-original-height="349" data-original-format="image/png" data-original-filesize="310708"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://iosdevweekly.com/" target="_blank" rel="nofollow">iOS Dev Weekly</a></h3>
<p>每周一期，包含于iOS开发相关的重要新闻，开发、设计、工具、市场、就业等各方面的优秀资源或文章。你可以通过邮件来进行订阅。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 404px;">
<div class="image-container-fill" style="padding-bottom: 48.209999999999994%;"></div>
<div class="image-view" data-width="838" data-height="404"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-60c00f340b7458bd.png" data-original-width="838" data-original-height="404" data-original-format="image/png" data-original-filesize="215392"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://ios-goodies.com/" target="_blank" rel="nofollow">iOS Goodies</a></h3>
<p>同样是每周一期，用一个非常简洁的页面，以参考链接的形式提供一周内iOS相关的文章、工具、设计、教学视频等内容。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 572px;">
<div class="image-container-fill" style="padding-bottom: 62.38%;"></div>
<div class="image-view" data-width="917" data-height="572"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-14e049f998442a40.png" data-original-width="917" data-original-height="572" data-original-format="image/png" data-original-filesize="108198"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=http://swiftdevweekly.co/" target="_blank" rel="nofollow">Swift Developer Weekly</a></h3>
<p>这个网站包含了大量Swfit开发者需要的代码示例，教程，书籍以及其他资源。你也可以通过邮件订阅它的内容，每周会有一期更新。</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 532px;">
<div class="image-container-fill" style="padding-bottom: 57.199999999999996%;"></div>
<div class="image-view" data-width="930" data-height="532"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-850f1daf5c27bfb6.png" data-original-width="930" data-original-height="532" data-original-format="image/png" data-original-filesize="83890"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3><a href="https://link.jianshu.com?t=https://itunes.apple.com/us/app/swifty-learn-to-code-in-swift!/id886315617?mt=8&amp;ign-mpt=uo%3D4" target="_blank" rel="nofollow">Swifty - Code Swift on your iPhone</a></h3>
<p>希望在手机或iPad上学习Swift语言？Swifty是你所想要的，通过它学习Swift语言，你可以感到很多学习的乐趣。</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 694px; max-height: 438px;">
<div class="image-container-fill" style="padding-bottom: 63.11%;"></div>
<div class="image-view" data-width="694" data-height="438"><img data-original-src="//upload-images.jianshu.io/upload_images/1399853-ef22a304f0bb58ac.png" data-original-width="694" data-original-height="438" data-original-format="image/png" data-original-filesize="196143"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<p>我已将以上资源分享到<a href="https://link.jianshu.com?t=http://jijiangshe.com/resource/91" target="_blank" rel="nofollow">技匠社</a>，需要的同学可访问获取</p>
<blockquote>
<p>简书签约作者：技匠，以上内容欢迎大家分享到朋友圈/微博等。如需转载，请通过我的微信公众号联系。谢谢大家！</p>
</blockquote>

          </div>
        </div>
    </div>

    <!-- 如果是付费文章，未购买，则显示购买按钮 -->

    <!-- 连载目录项 -->

    <!-- 如果是付费文章 -->
      <!-- 如果是付费连载，已购买，且作者允许赞赏，则显示付费信息和赞赏 -->
        <div data-vcomp="free-reward-panel"></div>

      <div class="show-foot">
        <a class="notebook" href="/nb/3655293">
          <i class="iconfont ic-search-notebook"></i>
          <span>技匠•工具</span>
</a>        <div class="copyright" data-toggle="tooltip" data-html="true" data-original-title="转载请联系作者获得授权，并标注“简书作者”。">
          © 著作权归作者所有
        </div>
        <div class="modal-wrap" data-report-note>
          <a id="report-modal">举报文章</a>
        </div>
      </div>

      <!-- 文章底部作者信息 -->
        <div class="follow-detail">
          <div class="info">
            <a class="avatar" href="/u/3313b20a4e25">
              <img src="//upload.jianshu.io/users/upload_avatars/1399853/1723bf426bd3.png?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96" alt="96" />
</a>            <div props-data-classes="user-follow-button-footer" data-author-follow-button></div>
            <a class="title" href="/u/3313b20a4e25">技匠</a>
              <img class="badge-icon" data-toggle="tooltip" title="程序员优秀作者" src="//upload.jianshu.io/user_badge/595a1b60-08f6-4beb-998f-2bf55e230555" alt="595a1b60 08f6 4beb 998f 2bf55e230555" />
              <i class="iconfont ic-man"></i>
          </div>
            <div class="signature">《程序员的自我修养》作者，微信订阅号：techmask

全栈工程师 | 技匠社创始人(jijiangshe.com) | 稀土掘金联合编辑 |51CTO特邀作者| 慕课签约作者 | 百度知道日报特邀作者 | LinkedIn专栏作者 | IT管理者

工作时我是一名IT管理者，下班后我是一名全栈工程师，做着自己喜欢的开源项目。很愿意与大家分享我在实践中获得的经验与感悟。
 

【已委托“维权骑士”为我的文章维权】</div>
        </div>

    <div class="meta-bottom">
      <div class="btn like-group"></div>
      <div class="share-group">
        <a class="share-circle" data-action="weixin-share" data-toggle="tooltip" data-original-title="分享到微信">
          <i class="iconfont ic-wechat"></i>
        </a>
        <a class="share-circle" data-action="weibo-share" data-toggle="tooltip" href="javascript:void((function(s,d,e,r,l,p,t,z,c){var%20f=&#39;http://v.t.sina.com.cn/share/share.php?appkey=1881139527&#39;,u=z||d.location,p=[&#39;&amp;url=&#39;,e(u),&#39;&amp;title=&#39;,e(t||d.title),&#39;&amp;source=&#39;,e(r),&#39;&amp;sourceUrl=&#39;,e(l),&#39;&amp;content=&#39;,c||&#39;gb2312&#39;,&#39;&amp;pic=&#39;,e(p||&#39;&#39;)].join(&#39;&#39;);function%20a(){if(!window.open([f,p].join(&#39;&#39;),&#39;mb&#39;,[&#39;toolbar=0,status=0,resizable=1,width=440,height=430,left=&#39;,(s.width-440)/2,&#39;,top=&#39;,(s.height-430)/2].join(&#39;&#39;)))u.href=[f,p].join(&#39;&#39;);};if(/Firefox/.test(navigator.userAgent))setTimeout(a,0);else%20a();})(screen,document,encodeURIComponent,&#39;&#39;,&#39;&#39;,&#39;&#39;, &#39;推荐 @技匠 的文章《iOS开发完全自学资源集合》（ 分享自 @简书 ）&#39;,&#39;https://www.jianshu.com/p/d70041eb25d7?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=weibo&#39;,&#39;页面编码gb2312|utf-8默认gb2312&#39;));" data-original-title="分享到微博">
          <i class="iconfont ic-weibo"></i>
        </a>
        <a class="share-circle" data-toggle="tooltip"  id="longshare" target="_blank">
            <div class="qrcode" id="qrcode">
             <img src="//cdn2.jianshu.io/assets/web/download-index-side-qrcode-cb13fc9106a478795f8d10f9f632fccf.png" alt="Download index side qrcode" />
             <p>下载app生成长微博图片</p>
             </div>
          <i class="iconfont ic-picture"></i>
        </a>
        <a class="share-circle more-share" tabindex="0" data-toggle="popover" data-placement="top" data-html="true" data-trigger="focus" href="javascript:void(0);" data-content='
          <ul class="share-list">
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=&#39;+e(&#39;https://www.jianshu.com/p/d70041eb25d7?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=qzone&#39;)+&#39;&amp;title=&#39;+e(&#39;推荐 技匠 的文章《iOS开发完全自学资源集合》&#39;),x=function(){if(!window.open(r,&#39;qzone&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=600,height=600&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-zone"></i><span>分享到QQ空间</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://twitter.com/share?url=&#39;+e(&#39;https://www.jianshu.com/p/d70041eb25d7?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=twitter&#39;)+&#39;&amp;text=&#39;+e(&#39;推荐 技匠 的文章《iOS开发完全自学资源集合》（ 分享自 @jianshucom ）&#39;)+&#39;&amp;related=&#39;+e(&#39;jianshucom&#39;),x=function(){if(!window.open(r,&#39;twitter&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=600,height=600&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-twitter"></i><span>分享到Twitter</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://www.facebook.com/dialog/share?app_id=483126645039390&amp;display=popup&amp;href=https://www.jianshu.com/p/d70041eb25d7?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=facebook&#39;,x=function(){if(!window.open(r,&#39;facebook&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-facebook"></i><span>分享到Facebook</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://plus.google.com/share?url=&#39;+e(&#39;https://www.jianshu.com/p/d70041eb25d7?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=google_plus&#39;),x=function(){if(!window.open(r,&#39;google_plus&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-google"></i><span>分享到Google+</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,s1=window.getSelection,s2=d.getSelection,s3=d.selection,s=s1?s1():s2?s2():s3?s3.createRange().text:&#39;&#39;,r=&#39;http://www.douban.com/recommend/?url=&#39;+e(&#39;https://www.jianshu.com/p/d70041eb25d7?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=douban&#39;)+&#39;&amp;title=&#39;+e(&#39;iOS开发完全自学资源集合&#39;)+&#39;&amp;sel=&#39;+e(s)+&#39;&amp;v=1&#39;,x=function(){if(!window.open(r,&#39;douban&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r+&#39;&amp;r=1&#39;};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})()"><i class="social-icon-sprite social-icon-douban"></i><span>分享到豆瓣</span></a></li>
          </ul>
        '>更多分享</a>
      </div>
    </div>
      <a id="web-note-ad-1" target="_blank" href="/apps/redirect?utm_source=note-bottom-click"><img src="//cdn2.jianshu.io/assets/web/web-note-ad-1-c2e1746859dbf03abe49248893c9bea4.png" alt="Web note ad 1" /></a>
    <div id="vue_comment"></div>
  </div>

  <div class="vue-side-tool" props-data-props-show-qr-code="0"></div>
</div>
<div class="note-bottom">
  <div class="js-included-collections"></div>
  <div data-vcomp="recommended-notes" data-lazy="1.5" data-note-id="3328010"></div>
  <!-- 相关文章 -->
  <div class="seo-recommended-notes">

        <div class="note ">
                    <a class="title" target="_blank" href="/p/2623ffb0d57a?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">iOS开发 非常全的三方库、插件、大牛博客等等</a>
          <p class="description">用到的组件1、通过CocoaPods安装项目名称项目信息AFNetworking网络请求组件FMDB本地数据库组件SDWebImage多个缩略图缓存组件UICKeyChainStore存放用户账号密码组件Reachability监测网络状态DateTools友好化时间MBP...</p>
          <a class="author" target="_blank" href="/u/c58eb2bd18c1?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/6175219/3aeefded-f349-4419-8b3b-6a4dbe69ba1b.jpeg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">frolaqi</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/fa0b6f594c36?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">iOS 第三方库、插件、知名博客总结</a>
          <p class="description">用到的组件1、通过CocoaPods安装项目名称项目信息 AFNetworking网络请求组件 FMDB本地数据库组件 SDWebImage多个缩略图缓存组件 UICKeyChainStore存放用户账号密码组件 Reachability监测网络状态 DateTools友好...</p>
          <a class="author" target="_blank" href="/u/524ab6e6e423?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/2969114/0251254d-7ca9-4ee9-9781-9096a492aa0b.jpeg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">大灰狼的小绵羊哥哥</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/0c0b3a9512e6?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">iOS开发 非常全的三方库、插件、大牛博客等等</a>
          <p class="description">UI 下拉刷新 EGOTableViewPullRefresh- 最早的下拉刷新控件。 SVPullToRefresh- 下拉刷新控件。 MJRefresh- 仅需一行代码就可以为UITableView或者CollectionView加上下拉刷新或者上拉刷新功能。可以自定义...</p>
          <a class="author" target="_blank" href="/u/e87b6147096c?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//cdn2.jianshu.io/assets/default_avatar/1-04bbeead395d74921af6a4e8214b4f61.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">俊洋洋</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/e1f980f07138?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">IOS开发  三方库</a>
          <p class="description">UI 下拉刷新 EGOTableViewPullRefresh- 最早的下拉刷新控件。 SVPullToRefresh- 下拉刷新控件。 MJRefresh- 仅需一行代码就可以为UITableView或者CollectionView加上下拉刷新或者上拉刷新功能。可以自定义...</p>
          <a class="author" target="_blank" href="/u/eab1f87934d5?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/6533814/e739bc0d-57af-4dd0-b8b2-6ebb8bc45075?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">毛毛萌</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/3c57951870b0?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">iOS开发第三方库汇总</a>
          <p class="description">前言 目前整理到常用的第三方库，仅供大家学习和参考使用，希望大家共同成长 具体内容 UI 下拉刷新 EGOTableViewPullRefresh - 最早的下拉刷新控件。 SVPullToRefresh - 下拉刷新控件。 MJRefresh - 仅需一行代码就可以为UI...</p>
          <a class="author" target="_blank" href="/u/28b239b99011?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/2901109/86061caa1008.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">BeSt2wazi</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/d082061df621?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">想要追到牛人，自己必须成为牛人</a>
          <p class="description">最近在罗辑思维的群里遇到一哥们，状态十分强烈，强烈到什么程度呢？不顾一切也要见罗振宇罗老师（简称罗胖）一面并问一个问题，看到他在群里发的那一切的时候我感到很是钦佩，这个人好有勇气，换做我肯定没有他的那种激情，可就在他见到罗胖的时候，我对他的态度发生了转变。 他与罗胖合了张照...</p>
          <a class="author" target="_blank" href="/u/093b7a136bad?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/3974885/d77532d43cd6?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">农村范儿ar</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/cd9f04df5550?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">广东人的祖先在南雄珠玑巷</a>
          <p class="description">提起珠玑巷，我们这一代人不甚了解，可是却经常被父辈带去韶关南雄珠玑巷寻根问祖。 对，珠玑巷位于广东最北边，可以说是穷山恶水，对于我们这些生长在富庶的珠三角的人来说，是不太愿意相信我们的祖先来自穷山区的。别笑这种心理，你得承认，没人喜欢穷亲戚。可是，我家的族谱上写得清清楚楚来...</p>
          <a class="author" target="_blank" href="/u/c5f59c3de37a?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/929607/86afe999f90c.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">深见江</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/87056a04eb14?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">想念好友之晋晋</a>
          <p class="description">     晋晋，一个20岁就生了美淇，当了妈的女人，有时做事看起来比较泼妇，但我就喜欢她的那种泼辣，跟她在一起如果我被人欺负，她会比任何人都着急要跟对方吵架，以至于她老公看她就是一泼妇，其实事实往往不是如宇哥所说那样，她在乎身边的每一个朋友，以至于张开羽翼保护身边人，不忍她...</p>
          <a class="author" target="_blank" href="/u/092ed37f6a43?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/7733265/1126aa30-56aa-4bd7-9859-947c79282657.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">artonice</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/3bc9f53f6711?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">Android linux系统644、755、777权限详解</a>
          <p class="description">转自：www.111cn.net/sys/linux/59979.htm 在linux系统中644、755、777三种权限是非常重要的一些权限了，下面我来详细的介绍644、755、777三种权限的使用，希望对各位有帮助。 常用的linux文件权限： 444 r--r--r-...</p>
          <a class="author" target="_blank" href="/u/f52e9b2dd596?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/5534080/16096509-c670-4565-89f8-f840a6f0cee5?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">xiaoyao1920</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/609da62d9732?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">对认为女人不应该上桌吃饭的人我想说的是</a>
          <p class="description">今天看到网上流传着一篇神作《在我老家，女人小孩不上桌的家庭更兴旺》看后实在无语，实在不能想象这是一个以文字谋生的人能够说出来的话。文中说一个家庭吃顿饭的时候男女老幼混杂是没“规矩”，失了面子。那么我想问一问，是小孩儿让你没了面子还是女人让你没了面子？小孩子小不懂事在饭桌上哭...</p>
          <a class="author" target="_blank" href="/u/9465dc13e891?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//cdn2.jianshu.io/assets/default_avatar/1-04bbeead395d74921af6a4e8214b4f61.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">猫小九儿</span>
</a>        </div>
  </div>
</div>

    <script type="application/json" data-name="page-data">{"user_signed_in":false,"locale":"zh-CN","os":"windows","read_mode":"day","read_font":"font2","note_show":{"is_author":false,"is_following_author":false,"is_liked_note":false,"follow_state":0,"uuid":"faf6add7-fb2f-4f83-ae54-8e6938a66673"},"note":{"id":3328010,"slug":"d70041eb25d7","user_id":1399853,"notebook_id":3655293,"commentable":true,"likes_count":1390,"views_count":37126,"public_wordage":1905,"comments_count":136,"featured_comments_count":0,"total_rewards_count":4,"is_author":false,"paid_type":"free","paid":false,"paid_content_accessible":false,"author":{"nickname":"技匠","total_wordage":176558,"followers_count":21606,"total_likes_count":28284}}}</script>
    
    <script src="//cdn2.jianshu.io/assets/babel-polyfill-e9c9b9785eb2c39c58e4.js" crossorigin="anonymous"></script>
    <script src="//cdn2.jianshu.io/assets/web-base-101dc0d8b4ed018d85d8.js" crossorigin="anonymous"></script>
<script src="//cdn2.jianshu.io/assets/web-ce06a7e26adb362dc9df.js" crossorigin="anonymous"></script>
    
    <script src="//cdn2.jianshu.io/assets/web/pages/notes/show/entry-30f3e70f59f62b93fe6b.js" crossorigin="anonymous"></script>
    <script>
  (function(){
      var bp = document.createElement('script');
      var curProtocol = window.location.protocol.split(':')[0];
      if (curProtocol === 'https') {
          bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
      }
      else {
          bp.src = 'http://push.zhanzhang.baidu.com/push.js';
      }
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(bp, s);
  })();
  

</script>
    <ol>
        <li class="special">this list item is special</li>
        <li class="special">this list item is also special</li>
        <li>this list item is not special</li>
    <ol>
  </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
d = soup.find_all('div')
# print(d)

d = soup.find_all(class_="tab ")
# print(d)

# id: # foo
# class:  .foo
# children: div > foo
# descendents: div p

d = soup.select('#menu')  # id="menu"
# print(d)

d = soup.select(".tab ")  # class_ = "tab "
# print(d)

d = soup.select("[data-vcomp]")  # attrs = {"data-vcomp": True}
# print(d)

d = soup.select('.special')
# for i in d:
#     print(i.get_text())
#     print(i.name)
#     print(i.attrs)

# print(soup.body.contents)

