$(document).ready(function(){
    "use strict";
	
	//Slide 1    
    var av = new JSAV("DemorganIntersect");
    av.umsg("Display Demorgan Algorithm");
    //av.nodes();
    av.displayInit();

    //Slide 2
    var urlLinkStep1 = "../../../AV/Yilu/figure.jff";
    var figure1 = new av.ds.FA({center:true, url: urlLinkStep1, left: 10, top:0, height: 500, width: 500});
    var figure2 = new av.ds.FA({center:true, url: urlLinkStep1, left: 10, top:200, width: 500});
    av.umsg("Start with two machines");
	av.step();


	//Slide 3
	figure1=FiniteAutomaton.complement(av, figure1, {center:true, left: 10, top:0, width: 500});
	figure2=FiniteAutomaton.complement(av, figure2, {center:true, left: 10, top:200, width: 500});
	av.umsg("Take complement of the two machines");
	av.step();


	//Slide 4
	var combined = FiniteAutomaton.combine(av, figure1, figure2, {left: 10, top:0, height: 450, width: 750});	
	var nodes = figure1.nodes();
	for (var next = nodes.next(); next; next = nodes.next()) {
      figure1.removeNode(next);
    }
    nodes = figure2.nodes();
    for (var next = nodes.next(); next; next = nodes.next()) {
      figure2.removeNode(next);
    }
    av.step();
	//Slide5
	var start = combined.addNode();
	combined.removeInitial(combined.initial);
    combined.makeInitial(start);
    combined.addEdge(start, combined.nodes()[0] /*newNodes[newOneStates.length]*/, {weight: lambda});
    combined.addEdge(start, combined.nodes()[3] /*newNodes[0]*/, {weight: lambda});
    combined.layout();
    av.umsg("Combine the two machines into one machine and take the union of them");
    av.step();

    //Slide 6
    combined.hide();
    var dfa = FiniteAutomaton.convertNFAtoDFA(av, combined, {top: 0, left: 10, width: 500, height: 150});
    dfa.layout();
    av.umsg("Convert the NFA machine to DFA")
	av.step();
	
	//Slide 7
	var mytree = new av.ds.tree({width: 400, height: 340, editable: true, left: 550, top: 0});
	mytree.hide();
  	combined.hide();
  	var minm = new Minimizer();
  	var minized = minm.minimizeDFA(av, dfa, mytree, {left: 10, top:0, height: 450, width: 750}, false);
  	minized.layout();
  	av.umsg("Then, minimize the DFA");
  	av.step();

  	//Slide 8
  	s = minized.initial;
  	minized = FiniteAutomaton.complement(av, minized, {left: 10, top:0, height: 450, width: 750});
    minized.makeInitial(s);
  	av.umsg("Finaly, take the complement of the minimized DFA so we will get the intersection");
  	av.recorded();
	/*
	//Slide 3
	figure1.hide();
	var urlLinkStep2 = "../../../AV/Yilu/figure2.jff";
	var figure2 = new av.ds.FA({center:true, url: urlLinkStep2, width: 600, height:600});
	av.umsg("Take the union of the two complemented machines");
	av.step();
	
	//Slide 4
	figure2.hide();
	var urlLinkStep3 = "../../../AV/Yilu/figure3.jff";
	var figure3 = new av.ds.FA({center:true, url: urlLinkStep3, width: 600, height:600});
	av.umsg("Convert it to DFA");
	av.step();
	
	//Slide 5
	figure3.hide();
	var urlLinkStep4 = "../../../AV/Yilu/figure4.jff";
	var figure4 = new av.ds.FA({center:true, url: urlLinkStep4, width: 600, height:600});
	av.umsg("Minimize the DFA");
	av.step();
	
	//Slide 6
	figure4.hide();
	var urlLinkStep5 = "../../../AV/Yilu/figure5.jff";
	var figure5 = new av.ds.FA({center:true, url: urlLinkStep5, width: 600, height:600});
	av.umsg("Take the complement");
	av.step();
	av.recorded();
	*/
});