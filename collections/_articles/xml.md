---
permalink: /articles/tutorial-xml-level-unity
boxclassname: black
author: "Gabor Szekeres"
topic: "Development, Tutorial"
title: "Tutorial – Roboust XML level building in Unity"
leadhead: "Having a robust process for loading levels is essential."
leadtext: "In theory we could save each level as a scene in Unity but it just not going to work once we have a couple of levels. Using serialized text i.e. JSON or XML is very convenient and probably the best thing to do if we also want to tweak the levels in a text editor."
image: /assets/images/articles/Unity.png
date: '2019-02-10 00:00:00'
---

<div class="arttext">
<p>There are a few areas that our XML serializer should address, i.e. default values, rounded values, etc:</p>
<h5>Default values for less clutter</h5>
<p>It makes sense to assume that the default position and rotation for any item is (0,0) with 0 degrees rotation.</p>
<p>For example let’s say we put a table at position (1,2), rotate it by 45 degrees and put a floor at position (0,0) scale it to (100,200) and do not rotate.</p>
<p>This is how an XML without default values would look like:</p>
<pre class="lang:default decode:true">&lt;Item prefab=”Table” x=”1” y=”2” rot=”45” scale_x=”1” scale_y=”1” /&gt; 
&lt;Item prefab=”Floor” x=”0” y=”0” rot=”0” scale_x=”100” scale_y=”200” /&gt;</pre>
<p>Now let’s cut off unnecessary stuff:</p>
<pre class="lang:default decode:true">&lt;Item prefab=”Table” x=”1” y=”2” rot=”45” /&gt; 
&lt;Item prefab=”Floor” scale_x=”100” scale_y=”200” /&gt;</pre>
<p>It looks heaps better and it’s easier to edit manually. At the same time it’s quite easy to read and write such XML as we just have to introduce a few lines of code as an internal layer between the XML and our GameObjects.</p>
<h5>Rounded values for easier manual tweak</h5>
<p>If we move an item to position (2.3423534, 1.39371945) we would would like to see rounded values after the serialization into XML, something like this below to ease manual tweaking later on.</p>
<pre class="lang:default decode:true">&lt;Item prefab=”Table” x=”2.34” y=”1.39” /&gt;</pre>
<h5>Cross checking prefabs in the XML file and the actual assets</h5>
<p>Once we have a lot of items it is easy to lose track of the assets that we referenced in the XML file and the actual Assets in Unity. If we have &lt;Item prefab=”Table” /&gt; in our XML but there is no corresponding Table prefab in the /Resources/Prefabs folder then we want to be warned in the development phase.</p>
<h3>Our objective</h3>
<p>In this example we will have two levels and will start with level one. We will load a capsule, two cubes and a sphere. This is how the XML looks like:</p>
<pre class="lang:default decode:true">&lt;?xml version="1.0" encoding="us-ascii"?&gt;

&lt;Levels&gt;

  &lt;Developer StartLevel="1" /&gt;

  &lt;Level&gt;
    &lt;Item prefab="BlueCapsule" x="1" y="2" /&gt;
    &lt;Item prefab="RedCube" x="4" y="1" rot="45" /&gt;
    &lt;Item prefab="RedCube" y="-2" rot="30" scale_y="3" /&gt;
    &lt;Item prefab="GreenSphere" x="-4" y="-2" /&gt;
  &lt;/Level&gt;

  &lt;Level&gt;
    &lt;Item prefab="BlueCapsule" x="0" /&gt;
    &lt;Item prefab="BlueCapsule" x="2" scale_y="1.2" /&gt;
    &lt;Item prefab="BlueCapsule" x="4" scale_y="1.4" /&gt;
    &lt;Item prefab="BlueCapsule" x="6" scale_y="1.6" /&gt;
  &lt;/Level&gt;

&lt;/Levels&gt;</pre>
<h3>Let&#8217;s do it in practice</h3>
<p>Download the working project (under 100 kB) with git or zip, they are both the same:</p>
<pre class="lang:default highlight:0 decode:true ">git clone https://github.com/TeamBrookvale/UnityXmlLevels.git</pre>
<p><a href="https://github.com/TeamBrookvale/UnityXmlLevels/archive/master.zip" title="UnityXmlLevels">https://github.com/TeamBrookvale/UnityXmlLevels/archive/master.zip</a></p>
<p>After downloading, follow the steps below:</p>
<ol>
<li>Open MainScene. You find it at Project pane -&gt; Assets -&gt; <em>LOADTHIS_SCENE</em> -&gt; MainScene</li>
<li>Click Window -&gt; &#8220;Xml Level Editor&#8221;</li>
<li>Delete all loaded XML files: Click on &#8220;Delete&#8221; button in the Xml Level Editor pane</li>
<li>Import again: Click on &#8220;Import Levels.xml&#8221; button in the Xml Level Editor pane</li>
<li>Create some prefabs and export them to XML:
<ol>
<li>Click on the &#8220;Export XmlItemsToExport&#8221; in the Xml Level Editor pane so an XmlItemsToExport GameObject is created in the Hierarchy pane</li>
<li>Open the Assets/Resources/Prefabs folder in the project pane</li>
<li>Drag and drop a few prefabs (e.g. BlueCapsule) on XmlItemsToExport in the Hierarchy pane and move them to random positions</li>
<li>Once it&#8217;s done click again on &#8220;Export XmlItemsToExport&#8221;</li>
<li>Now there should be an <strong>XmlItemsToExport.xml</strong> file in the Resources folder. It should contain the child items of XmlItemsToExport GameObject. You can copy and paste the items back into the <strong>Levels.xml</strong> file. The contents of the <strong>Levels.xml</strong> file is loaded upon hitting play or clicking on &#8220;Import Levels.xml&#8221; button on the Xml Level Editor pane.</li>
</ol>
</li>
<li>Play around with the Cross Checker in the Xml Level Editor pane. Just add a few dummy items to your Levels.xml e.g. &lt;Item prefab=”NotExisting” /&gt;. Click on and the &#8220;Cross Check&#8221; button in the Xml Level Editor pane and you will be warned in the Console about the missing NotExisting prefab.</li>
<li>Done</li>
</ol>
<a href="/assets/images/articles/Unity.png"><img src="/assets/images/articles/Unity.png" alt="unity" /></a><p>Unity Xml Levels Screenshot</p>
<p>That&#8217;s it. Have a look at the main files below to understand what&#8217;s happening under the hood:</p>
<table>
<thead>
<tr>
<th>File</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>Levels.xml</td>
<td>All levels in XML format</td>
</tr>
<tr>
<td>DeserializedLevels.cs</td>
<td>C# class representation of the XML structure</td>
</tr>
<tr>
<td>DeserializedLevelsLoader.cs</td>
<td>Generates items from Levels.xml</td>
</tr>
<tr>
<td>DeserializedLevelsSaver.cs</td>
<td>Saves to XmlItemsToExport.xml</td>
</tr>
<tr>
<td>DeserializedLevelsCrossChecker.cs</td>
<td>Cross checks /Resources/Prefabs and Levels.xml</td>
</tr>
<tr>
<td>XmlIO.cs</td>
<td>Handles XML file operations</td>
</tr>
<tr>
<td>XmlLevelEditor.cs</td>
<td>Buttons and labels for the Xml Level Editor pane</td>
</tr>
</tbody>
</table>
<p>Good luck and feel free to share thoughts or ask questions.</p>
</div>