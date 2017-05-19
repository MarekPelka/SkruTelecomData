package com.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class GoogleController {
	@RequestMapping(value = {"/rawdata/googlemap/{squareId}","/proceededdata/googlemap/{squareId}"}, method = RequestMethod.GET)
	public ModelAndView getGoogleMap(@PathVariable("squareId") int squareId) {
		ModelAndView model = new ModelAndView("googlemap");
		double coordinatex0 = 9.011490619692509;
		double coordinatey0 = 45.356685994655464;
		int xdelta = squareId % 100;
		double resultCoordinateX = coordinatex0 + xdelta*( 9.311521155996243-9.011490619692509);
		int ydelta = squareId / 100;
		double resultCoordinateY = coordinatey0 + ydelta*( 45.56778671132765-45.356261753717845);
		model.addObject("leftBottomX", resultCoordinateX);
		model.addObject("leftBottomY", resultCoordinateY);
		
		model.addObject("leftTopX", resultCoordinateX);
		model.addObject("leftTopY", resultCoordinateY + ( 45.56778671132765-45.356261753717845)/100.0);
		
		model.addObject("rightBottomX", resultCoordinateX + (9.311521155996243-9.011490619692509)/100.0);
		model.addObject("rightBottomY", resultCoordinateY);
		
		model.addObject("rightTopX", resultCoordinateX + (9.311521155996243-9.011490619692509)/100.0);
		model.addObject("rightTopY", resultCoordinateY + ( 45.56778671132765-45.356261753717845)/100.0);
		return model;
	}
}
