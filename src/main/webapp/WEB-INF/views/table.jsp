<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<html>
<head>
<title>Proceeded data page</title>
<link href="<c:url value='/css/bootstrap.css' />" rel="stylesheet"></link>
<link href="<c:url value='/css/app.css' />" rel="stylesheet"></link>
<link rel="stylesheet" type="text/css"
	href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.2.0/css/font-awesome.css" />
<link rel="stylesheet"
	href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<link rel="stylesheet" href="/resources/demos/style.css">
<link rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<style>
h1 {
	color: white;
	font-family: 'Helvetica Neue', sans-serif;
	font-size: 46px;
	font-weight: 100;
	line-height: 50px;
	letter-spacing: 1px;
	padding: 0 0 5px;
	border-bottom: double #555;
}
</style>
</head>
<body>
	<div id="mainWrapper">
		<div class="my-container">
			<div align="center">
				<h1>Biggest daily average</h1>
				<table border=1>
					<tr>
						<th>No.</th>
						<th>SMS in</th>
						<th>SMS out</th>
						<th>Call in</th>
						<th>Call out</th>
						<th>Internet traffic</th>
					</tr>
					<tr>
						<td>1</td>
						<td>20 Dec</td>
						<td>25 Dec</td>
						<td>20 Dec</td>
						<td>20 Dec</td>
						<td>11 Nov</td>
					</tr>
					<tr>
						<td>2</td>
						<td>27 Nov</td>
						<td>24 Dec</td>
						<td>16 Dec</td>
						<td>16 Dec</td>
						<td>10 Nov</td>
					</tr>
					<tr>
						<td>3</td>
						<td>22 Nov</td>
						<td>01 Jan</td>
						<td>23 Dec</td>
						<td>23 Dec</td>
						<td>12 Nov</td>
					</tr>
					<tr>
						<td>4</td>
						<td>13 Dec</td>
						<td>11 Nov</td>
						<td>19 Dec</td>
						<td>19 Dec</td>
						<td>09 Nov</td>
					</tr>
					<tr>
						<td>5</td>
						<td>08 Nov</td>
						<td>19 Nov</td>
						<td>18 Dec</td>
						<td>18 Dec</td>
						<td>04 Nov</td>
					</tr>
				</table>


				<h1>Smallest daily average</h1>
				<table border=1>
					<tr>
						<th>No.</th>
						<th>SMS in</th>
						<th>SMS out</th>
						<th>Call in</th>
						<th>Call out</th>
						<th>Internet traffic</th>
					</tr>
					<tr>
						<td>1</td>
						<td>29 Dec</td>
						<td>29 Dec</td>
						<td>26 Dec</td>
						<td>26 Dec</td>
						<td>01 Jan</td>
					</tr>
					<tr>
						<td>2</td>
						<td>26 Dec</td>
						<td>28 Dec</td>
						<td>01 Jan</td>
						<td>01 Jan</td>
						<td>31 Dec</td>
					</tr>
					<tr>
						<td>3</td>
						<td>28 Dec</td>
						<td>30 Dec</td>
						<td>29 Dec</td>
						<td>29 Dec</td>
						<td>25 Dec</td>
					</tr>
					<tr>
						<td>4</td>
						<td>03 Nov</td>
						<td>27 Dec</td>
						<td>03 Nov</td>
						<td>03 Nov</td>
						<td>30 Dec</td>
					</tr>
					<tr>
						<td>5</td>
						<td>17 Nov</td>
						<td>26 Dec</td>
						<td>25 Dec</td>
						<td>25 Dec</td>
						<td>29 Dec</td>
					</tr>
				</table>
			</div>
		</div>
	</div>

</body>
</html>
