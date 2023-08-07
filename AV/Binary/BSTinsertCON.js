/*global ODSA */
// Insert slideshow
$(document).ready(function() {
  "use strict";
  var av_name = "BSTinsertCON";
  var config = ODSA.UTILS.loadConfig({av_name: av_name}),
      interpret = config.interpreter,       // get the interpreter
      code = config.code;                   // get the code object
  var av = new JSAV(av_name);
//  var pseudo = av.code($.extend({top: -50, left: 200}, code[0]));
  var pseudo = av.code(code[0]);

  var bt = av.ds.binarytree({visible: true, nodegap: 15});
  bt.root(37);
  var rt = bt.root();
  rt.left(24);
  rt.left().left(7);
  rt.left().left().left(2);
  rt.left().right(32);
  rt.right(42);
  rt.right().left(42);
  rt.right().left().left(40);
  rt.right().right(120);
  var newnode = rt.left().right().left(30);
  newnode.addClass("invisnode");
  var newParent = newnode.parent();
  var newedge = newParent.edgeToLeft();
  newedge.hide();
  newedge.addClass("rededge");
  bt.layout();

  var rt1 = av.pointer("rt", bt.root(), {anchor: "right top", top: -10});

  // Slide 1
  av.umsg(interpret("sc1"));
  pseudo.highlight([2, 5])
  av.displayInit();

  // Slide 2
  av.umsg(interpret("sc2"));
  pseudo.unhighlight([2, 5])
  pseudo.highlight(6)
  av.step();

  // Slide 3
  av.umsg(interpret("sc3"));
  pseudo.unhighlight(6)
  pseudo.highlight(8)
  av.step();

  // Slide 4
  av.umsg(interpret("sc4"));
  av.step();

  // Slide 5
  av.umsg(interpret("sc5"));
  pseudo.unhighlight(8)
  pseudo.highlight(9)
  bt.root().addClass("processing");
  rt1.target(bt.root().left(), {anchor: "left top"});
  av.step();

  // Slide 6
  av.umsg(interpret("sc2"));
  pseudo.unhighlight(9)
  pseudo.highlight(6)
  av.step();

  // Slide 7
  av.umsg(interpret("sc7"));
  pseudo.unhighlight(6)
  pseudo.highlight(10)
  av.step();

  // Slide 8
  av.umsg(interpret("sc8"));
  av.step();

  // Slide 9
  av.umsg(interpret("sc9"));
  pseudo.unhighlight(10)
  pseudo.highlight(11)
  bt.root().left().addClass("processing");
  rt1.target(bt.root().left().right(), {anchor: "right top"});
  av.step();

  // Slide 10
  av.umsg(interpret("sc2"));
  pseudo.unhighlight(11)
  pseudo.highlight(6)
  av.step();

  // Slide 11
  av.umsg(interpret("sc3"));
  pseudo.unhighlight(6)
  pseudo.highlight(8)
  av.step();

  // Slide 12
  av.umsg(interpret("sc4"));
  av.step();

  // Slide 13
  av.umsg(interpret("sc5"));
  pseudo.unhighlight(8)
  pseudo.highlight(9)
  bt.root().left().right().addClass("processing");
  rt1.target(newnode, {anchor: "left top"});
  av.step();

  // Slide 14
  av.umsg(interpret("sc14"));
  pseudo.unhighlight(9)
  pseudo.highlight([6, 7])
  newnode.show();
  newnode.removeClass("invisnode");
  newnode.addClass("rednode");
  newedge.hide();
  av.step();

  // Slide 15
  av.umsg(interpret("sc15"));
  pseudo.unhighlight([6, 7])
  pseudo.highlight(12)
  av.step();

  // Slide 16
  av.umsg(interpret("sc16"));
  newnode = newnode.parent();
  newedge.show();
  bt.root().left().right().removeClass("processing");
  rt1.target(newnode, {anchor: "left top"});
  pseudo.unhighlight(12)
  pseudo.highlight(9)
  av.step();

  // Slide 17
  av.umsg(interpret("sc17"));
  newedge = newnode.edgeToParent();
  newnode = newnode.parent();
  newedge.addClass("rededge");
  bt.root().left().removeClass("processing");
  rt1.target(newnode, {anchor: "left top"});
  pseudo.unhighlight(9)
  pseudo.highlight(11)
  av.step();

  // Slide 18
  av.umsg(interpret("sc18"));
  newedge = newnode.edgeToParent();
  newnode = newnode.parent();
  newedge.addClass("rededge");
  bt.root().removeClass("processing");
  rt1.target(newnode, {anchor: "left top"});
  pseudo.unhighlight(11)
  pseudo.highlight(9)
  av.step();

  // Slide 19
  av.umsg(interpret("sc19"));
  rt1.hide();
  var root1 = av.pointer("root", bt.root(), {anchor: "right top", top: -10});
  root1.arrow.addClass("thinredline");
  // This line should not be needed, but it is here to fix Raphael bug with arrows
  root1.arrow.css({stroke: "red"});
  pseudo.unhighlight(9)
  pseudo.highlight(2)
  av.recorded();
});
