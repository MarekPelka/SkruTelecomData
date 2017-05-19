package com.controllers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.model.SelectionData;
import com.model.StatisticData;
import com.services.StatisticDataService;

@Controller
@RequestMapping("/proceededdata")
public class ProceededDataController {
	private static final String LIST_NAME = "valueList";
	private StatisticDataService statisticDataService;

	@Autowired(required = true)
	public void setStatisticDataService(StatisticDataService statisticDataService) {
		this.statisticDataService = statisticDataService;
	}

	@RequestMapping(value = "/chooser", method = RequestMethod.GET)
	public String datachooser(Model model) {
		model.addAttribute("selectionData", new SelectionData());
		return "proceededchooser";
	}

	@RequestMapping(value = "/chooser", method = RequestMethod.POST)
	public ModelAndView getAverages(@ModelAttribute("selectionData") SelectionData selectionData) {
		ModelAndView model = new ModelAndView("maprenderer");
		List<StatisticData> prodeededData = statisticDataService.getAveragesData();
		switch (selectionData.getProceededData()) {
		case "averages":
			prodeededData = statisticDataService.getAveragesData();
			break;
		}
		Collections.sort(prodeededData, (a1, a2) -> a1.getSquareId().compareTo(a2.getSquareId()));

		List<Double> valueList = new ArrayList<>();
		for (int i = 0; i < 10000; i++) {
			valueList.add(0.0);
		}

		switch (selectionData.getWhichData()) {
		case "smsin":
			model.addObject(LIST_NAME,
					prodeededData.stream().map(StatisticData::getSmsIn).collect(Collectors.toList()));
			break;
		case "smsout":
			model.addObject(LIST_NAME,
					prodeededData.stream().map(StatisticData::getSmsOut).collect(Collectors.toList()));
			break;
		case "callin":
			model.addObject(LIST_NAME,
					prodeededData.stream().map(StatisticData::getCallIn).collect(Collectors.toList()));
			break;
		case "callout":
			model.addObject(LIST_NAME,
					prodeededData.stream().map(StatisticData::getCallOut).collect(Collectors.toList()));
			break;
		case "internettraffic":
			model.addObject(LIST_NAME,
					prodeededData.stream().map(StatisticData::getInternetTraffic).collect(Collectors.toList()));
			break;
		default:
			model.addObject(LIST_NAME, valueList);
			break;
		}

		return model;
	}

}
