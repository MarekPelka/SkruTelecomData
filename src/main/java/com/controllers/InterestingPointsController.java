package com.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
@RequestMapping("/points")
public class InterestingPointsController {
	@RequestMapping(value = "/table", method = RequestMethod.GET)
	public String getTable() {
		return "table";
	}
}
