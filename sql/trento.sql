CREATE TABLE `trento` (
 `data_id` int(11) NOT NULL AUTO_INCREMENT,
 `square_id` int(11) NOT NULL,
 `time` bigint(11) NOT NULL,
 `country_code` varchar(20) NOT NULL,
 `sms_in` double NOT NULL,
 `sms_out` double NOT NULL,
 `call_in` double NOT NULL,
 `call_out` double NOT NULL,
 `internet_traffic` double NOT NULL,
 PRIMARY KEY (`data_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1