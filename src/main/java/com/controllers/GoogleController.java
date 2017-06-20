package com.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class GoogleController {
	@RequestMapping(value = {"/rawdata/googlemap/{squareId}","/proceededdata/googlemap/{squareId}","/googlemap/{squareId}"}, method = RequestMethod.GET)
	public ModelAndView getGoogleMap(@PathVariable("squareId") int squareId) {
		ModelAndView model = new ModelAndView("googlemap");
		double coordinatex0 = 9.011490619692509;
		double coordinatey0 = 45.356685994655464;
		int xdelta = squareId % 100;
		double resultCoordinateX = coordinatex0 + xdelta*0.0030119764449;
		int ydelta = squareId / 100;
		double resultCoordinateY = coordinatey0 + ydelta*0.0021110071667;
		
		model.addObject("leftBottomX", resultCoordinateX);
		model.addObject("leftBottomY", resultCoordinateY);
		
		model.addObject("leftTopX", resultCoordinateX);
		model.addObject("leftTopY", resultCoordinateY  + 0.0021110071667);
		
		model.addObject("rightBottomX", resultCoordinateX + 0.0030119764449);
		model.addObject("rightBottomY", resultCoordinateY);
		
		model.addObject("rightTopX", resultCoordinateX + 0.0030119764449);
		model.addObject("rightTopY", resultCoordinateY + 0.0021110071667);
		
		model.addObject("centerX", resultCoordinateX + 0.0030119764449/2);
		model.addObject("centerY", resultCoordinateY + 0.0021110071667/2);
		return model;
	}
}
