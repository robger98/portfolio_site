<script>
let { height, width } = $props();
let final_width = $derived(width - 32);// Render Plotly plots, called when the Plotly script is loaded
	const renderPlotly = () => {
		/* Plotly Plots */
        Plotly.newPlot('plotly_14_0', [{"alignmentgroup":"True","boxpoints":"all","customdata":[["heavy cavalry",50],["heavy cavalry",50],["heavy cavalry",50],["heavy cavalry",50]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>Damage x Toughness x Size=%{y}<br>Size=%{customdata[1]}<extra></extra>","hovertext":["Kataphraktoi","Tarkhans","Monaspa","Conrois"],"legendgroup":"heavy cavalry","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#636efa"},"name":"heavy cavalry","offsetgroup":"heavy cavalry","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[210000,165000,165000,125000],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["heavy infantry",100],["heavy infantry",100],["heavy infantry",100],["heavy infantry",100],["heavy infantry",100],["heavy infantry",100],["heavy infantry",100],["heavy infantry",100],["heavy infantry",100],["heavy infantry",50],["heavy infantry",100]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>Damage x Toughness x Size=%{y}<br>Size=%{customdata[1]}<extra></extra>","hovertext":["Varangian Veterans","Druzhina","Mubarizun","Mountaineers","Huscarls","Lenkas","Khandayat","Palace Guards","Zbrojnosh","Ayyar","Akritai"],"legendgroup":"heavy infantry","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#EF553B"},"name":"heavy infantry","offsetgroup":"heavy infantry","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[135000,120000,112500,104000,104000,92400,92400,91200,68000,38500,14000],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["horse archers",100]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>Damage x Toughness x Size=%{y}<br>Size=%{customdata[1]}<extra></extra>","hovertext":["Horse Archers"],"legendgroup":"horse archers","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#00cc96"},"name":"horse archers","offsetgroup":"horse archers","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[90000],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["light cavalry",50],["light cavalry",100],["light cavalry",100],["light cavalry",100]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>Damage x Toughness x Size=%{y}<br>Size=%{customdata[1]}<extra></extra>","hovertext":["Ayrudzi","Konni","Tawashi","Mulathanūm"],"legendgroup":"light cavalry","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#ab63fa"},"name":"light cavalry","offsetgroup":"light cavalry","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[75000,37500,37500,33000],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["pikemen",100],["pikemen",100],["pikemen",100]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>Damage x Toughness x Size=%{y}<br>Size=%{customdata[1]}<extra></extra>","hovertext":["Skoutatoi","Zupin Spearmen","Bondi"],"legendgroup":"pikemen","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#FFA15A"},"name":"pikemen","offsetgroup":"pikemen","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[57200,25600,25200],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["archers",100],["archers",100],["archers",100],["archers",100],["archers",50],["archers",100]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>Damage x Toughness x Size=%{y}<br>Size=%{customdata[1]}<extra></extra>","hovertext":["Metsänvartija","Nile Archers","Bush Hunters","Vigmen","Ballistrai","Longbowmen"],"legendgroup":"archers","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#19d3f3"},"name":"archers","offsetgroup":"archers","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[42000,42000,36000,36000,19250,16000],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["light infantry",100],["light infantry",100],["light infantry",100],["light infantry",100]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>Damage x Toughness x Size=%{y}<br>Size=%{customdata[1]}<extra></extra>","hovertext":["Abudrar","Guinean Uplanders","Shomer","Horn Warriors"],"legendgroup":"light infantry","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#FF6692"},"name":"light infantry","offsetgroup":"light infantry","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[32000,25200,24000,19200],"y0":" ","yaxis":"y"}], {"boxmode":"group","height":height,"legend":{"title":{"text":"Type"},"tracegroupgap":0},"template":{"data":{"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"heatmap"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermap":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermap"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"sequentialminus":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2}}},"title":{"text":"Most Effective MaA in CK3"},"width":final_width,"xaxis":{"anchor":"y","domain":[0,1]},"yaxis":{"anchor":"x","domain":[0,1],"title":{"text":"Damage x Toughness x Size"}}});
Plotly.newPlot('plotly_16_0', [{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=heavy cavalry<br>Damage x Size=%{x}<br>Toughness x Size=%{y}<extra></extra>","hovertext":["Kataphraktoi","Tarkhans","Monaspa","Conrois"],"legendgroup":"heavy cavalry","marker":{"color":"#636efa","symbol":"circle"},"mode":"markers","name":"heavy cavalry","orientation":"v","showlegend":true,"type":"scatter","x":[6000,5500,5500,5000],"xaxis":"x","y":[1750,1500,1500,1250],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=heavy infantry<br>Damage x Size=%{x}<br>Toughness x Size=%{y}<extra></extra>","hovertext":["Varangian Veterans","Druzhina","Mubarizun","Mountaineers","Huscarls","Lenkas","Khandayat","Palace Guards","Zbrojnosh","Ayyar","Akritai"],"legendgroup":"heavy infantry","marker":{"color":"#EF553B","symbol":"circle"},"mode":"markers","name":"heavy infantry","orientation":"v","showlegend":true,"type":"scatter","x":[4500,4000,4500,4000,4000,4200,4200,3800,3400,1750,1000],"xaxis":"x","y":[3000,3000,2500,2600,2600,2200,2200,2400,2000,1100,1400],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=horse archers<br>Damage x Size=%{x}<br>Toughness x Size=%{y}<extra></extra>","hovertext":["Horse Archers"],"legendgroup":"horse archers","marker":{"color":"#00cc96","symbol":"circle"},"mode":"markers","name":"horse archers","orientation":"v","showlegend":true,"type":"scatter","x":[4500],"xaxis":"x","y":[2000],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=light cavalry<br>Damage x Size=%{x}<br>Toughness x Size=%{y}<extra></extra>","hovertext":["Ayrudzi","Konni","Tawashi","Mulathanūm"],"legendgroup":"light cavalry","marker":{"color":"#ab63fa","symbol":"circle"},"mode":"markers","name":"light cavalry","orientation":"v","showlegend":true,"type":"scatter","x":[2500,2500,2500,2200],"xaxis":"x","y":[1500,1500,1500,1500],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=pikemen<br>Damage x Size=%{x}<br>Toughness x Size=%{y}<extra></extra>","hovertext":["Skoutatoi","Zupin Spearmen","Bondi"],"legendgroup":"pikemen","marker":{"color":"#FFA15A","symbol":"circle"},"mode":"markers","name":"pikemen","orientation":"v","showlegend":true,"type":"scatter","x":[2200,1600,1400],"xaxis":"x","y":[2600,1600,1800],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=archers<br>Damage x Size=%{x}<br>Toughness x Size=%{y}<extra></extra>","hovertext":["Metsänvartija","Nile Archers","Bush Hunters","Vigmen","Ballistrai","Longbowmen"],"legendgroup":"archers","marker":{"color":"#19d3f3","symbol":"circle"},"mode":"markers","name":"archers","orientation":"v","showlegend":true,"type":"scatter","x":[3000,3000,3000,1800,1750,2000],"xaxis":"x","y":[1400,1400,1200,2000,550,800],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=light infantry<br>Damage x Size=%{x}<br>Toughness x Size=%{y}<extra></extra>","hovertext":["Abudrar","Guinean Uplanders","Shomer","Horn Warriors"],"legendgroup":"light infantry","marker":{"color":"#FF6692","symbol":"circle"},"mode":"markers","name":"light infantry","orientation":"v","showlegend":true,"type":"scatter","x":[2000,1800,1000,1200],"xaxis":"x","y":[1600,1400,2400,1600],"yaxis":"y"}], {"height":height,"legend":{"title":{"text":"Type"},"tracegroupgap":0},"shapes":[{"opacity":0.5,"type":"line","x0":0,"x1":6600.000000000001,"xref":"x","y0":0,"y1":3300.0000000000005,"yref":"y"}],"template":{"data":{"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"heatmap"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermap":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermap"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"sequentialminus":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2}}},"title":{"text":"Damage vs. Toughness Trade-off"},"width":final_width,"xaxis":{"anchor":"y","domain":[0,1],"title":{"text":"Damage x Size"}},"yaxis":{"anchor":"x","domain":[0,1],"title":{"text":"Toughness x Size"}}});
Plotly.newPlot('plotly_20_0', [{"alignmentgroup":"True","boxpoints":"all","customdata":[["heavy infantry",100,1.44],["heavy infantry",100,1.56],["heavy infantry",100,1.44],["heavy infantry",100,1.53],["heavy infantry",100,2],["heavy infantry",100,1.44],["heavy infantry",100,1.44],["heavy infantry",100,1.54],["heavy infantry",100,1.32],["heavy infantry",50,1.08],["heavy infantry",100,0.41]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>(Damage x Toughness x Size) / Maintenance Cost=%{y}<br>Size=%{customdata[1]}<br>Raised maintenance=%{customdata[2]}<extra></extra>","hovertext":["Mubarizun","Druzhina","Mountaineers","Huscarls","Varangian Veterans","Khandayat","Palace Guards","Lenkas","Zbrojnosh","Ayyar","Akritai"],"legendgroup":"heavy infantry","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#636efa"},"name":"heavy infantry","offsetgroup":"heavy infantry","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[78125,76923.07692307692,72222.22222222222,67973.85620915033,67500,64166.66666666667,63333.333333333336,60000,51515.15151515151,35648.148148148146,34146.34146341464],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["heavy cavalry",50,2.73],["heavy cavalry",50,1.78],["heavy cavalry",50,2.62],["heavy cavalry",50,2.73]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>(Damage x Toughness x Size) / Maintenance Cost=%{y}<br>Size=%{customdata[1]}<br>Raised maintenance=%{customdata[2]}<extra></extra>","hovertext":["Kataphraktoi","Conrois","Monaspa","Tarkhans"],"legendgroup":"heavy cavalry","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#EF553B"},"name":"heavy cavalry","offsetgroup":"heavy cavalry","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[76923.07692307692,70224.7191011236,62977.09923664122,60439.56043956044],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["light cavalry",50,1.05],["light cavalry",100,1.15],["light cavalry",100,1.15],["light cavalry",100,1.36]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>(Damage x Toughness x Size) / Maintenance Cost=%{y}<br>Size=%{customdata[1]}<br>Raised maintenance=%{customdata[2]}<extra></extra>","hovertext":["Ayrudzi","Tawashi","Mulathanūm","Konni"],"legendgroup":"light cavalry","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#00cc96"},"name":"light cavalry","offsetgroup":"light cavalry","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[71428.57142857142,32608.695652173916,28695.652173913044,27573.529411764703],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["horse archers",100,1.35]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>(Damage x Toughness x Size) / Maintenance Cost=%{y}<br>Size=%{customdata[1]}<br>Raised maintenance=%{customdata[2]}<extra></extra>","hovertext":["Horse Archers"],"legendgroup":"horse archers","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#ab63fa"},"name":"horse archers","offsetgroup":"horse archers","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[66666.66666666666],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["archers",100,0.66],["archers",100,0.66],["archers",100,0.66],["archers",100,0.66],["archers",50,0.45],["archers",100,0.72]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>(Damage x Toughness x Size) / Maintenance Cost=%{y}<br>Size=%{customdata[1]}<br>Raised maintenance=%{customdata[2]}<extra></extra>","hovertext":["Metsänvartija","Nile Archers","Vigmen","Bush Hunters","Ballistrai","Longbowmen"],"legendgroup":"archers","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#FFA15A"},"name":"archers","offsetgroup":"archers","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[63636.36363636363,63636.36363636363,54545.454545454544,54545.454545454544,42777.777777777774,22222.222222222223],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["pikemen",100,0.99],["pikemen",100,0.6],["pikemen",100,0.6]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>(Damage x Toughness x Size) / Maintenance Cost=%{y}<br>Size=%{customdata[1]}<br>Raised maintenance=%{customdata[2]}<extra></extra>","hovertext":["Skoutatoi","Zupin Spearmen","Bondi"],"legendgroup":"pikemen","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#19d3f3"},"name":"pikemen","offsetgroup":"pikemen","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[57777.77777777778,42666.66666666667,42000],"y0":" ","yaxis":"y"},{"alignmentgroup":"True","boxpoints":"all","customdata":[["light infantry",100,0.45],["light infantry",100,0.54],["light infantry",100,0.45],["light infantry",100,0.81]],"fillcolor":"rgba(255,255,255,0)","hoveron":"points","hovertemplate":"<b>%{hovertext}</b><br><br>Type=%{customdata[0]}<br>(Damage x Toughness x Size) / Maintenance Cost=%{y}<br>Size=%{customdata[1]}<br>Raised maintenance=%{customdata[2]}<extra></extra>","hovertext":["Shomer","Guinean Uplanders","Horn Warriors","Abudrar"],"legendgroup":"light infantry","line":{"color":"rgba(255,255,255,0)"},"marker":{"color":"#FF6692"},"name":"light infantry","offsetgroup":"light infantry","orientation":"v","pointpos":0,"showlegend":true,"type":"box","x0":" ","xaxis":"x","y":[53333.33333333333,46666.666666666664,42666.666666666664,39506.17283950617],"y0":" ","yaxis":"y"}], {"boxmode":"group","height":height,"legend":{"title":{"text":"Type"},"tracegroupgap":0},"template":{"data":{"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"heatmap"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermap":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermap"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"sequentialminus":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2}}},"title":{"text":"Most Effective MaA in CK3 Per Gold"},"width":final_width,"xaxis":{"anchor":"y","domain":[0,1]},"yaxis":{"anchor":"x","domain":[0,1],"title":{"text":"(Damage x Toughness x Size) / Maintenance Cost"}}});
Plotly.newPlot('plotly_22_0', [{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=heavy infantry<br>Damage x Size / Maintenance Cost=%{x}<br>Toughness x Size / Maintenance Cost=%{y}<extra></extra>","hovertext":["Mubarizun","Druzhina","Mountaineers","Huscarls","Varangian Veterans","Khandayat","Palace Guards","Lenkas","Zbrojnosh","Ayyar","Akritai"],"legendgroup":"heavy infantry","marker":{"color":"#636efa","symbol":"circle"},"mode":"markers","name":"heavy infantry","orientation":"v","showlegend":true,"type":"scatter","x":[3125,2564.102564102564,2777.777777777778,2614.37908496732,2250,2916.666666666667,2638.888888888889,2727.272727272727,2575.7575757575755,1620.3703703703702,2439.0243902439024],"xaxis":"x","y":[1736.111111111111,1923.076923076923,1805.5555555555557,1699.3464052287582,1500,1527.7777777777778,1666.6666666666667,1428.5714285714284,1515.151515151515,1018.5185185185185,3414.6341463414637],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=heavy cavalry<br>Damage x Size / Maintenance Cost=%{x}<br>Toughness x Size / Maintenance Cost=%{y}<extra></extra>","hovertext":["Kataphraktoi","Conrois","Monaspa","Tarkhans"],"legendgroup":"heavy cavalry","marker":{"color":"#EF553B","symbol":"circle"},"mode":"markers","name":"heavy cavalry","orientation":"v","showlegend":true,"type":"scatter","x":[2197.802197802198,2808.9887640449438,2099.236641221374,2014.6520146520147],"xaxis":"x","y":[641.025641025641,702.2471910112359,572.5190839694657,549.4505494505495],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=light cavalry<br>Damage x Size / Maintenance Cost=%{x}<br>Toughness x Size / Maintenance Cost=%{y}<extra></extra>","hovertext":["Ayrudzi","Tawashi","Mulathanūm","Konni"],"legendgroup":"light cavalry","marker":{"color":"#00cc96","symbol":"circle"},"mode":"markers","name":"light cavalry","orientation":"v","showlegend":true,"type":"scatter","x":[2380.9523809523807,2173.913043478261,1913.0434782608697,1838.2352941176468],"xaxis":"x","y":[1428.5714285714284,1304.3478260869567,1304.3478260869567,1102.941176470588],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=horse archers<br>Damage x Size / Maintenance Cost=%{x}<br>Toughness x Size / Maintenance Cost=%{y}<extra></extra>","hovertext":["Horse Archers"],"legendgroup":"horse archers","marker":{"color":"#ab63fa","symbol":"circle"},"mode":"markers","name":"horse archers","orientation":"v","showlegend":true,"type":"scatter","x":[3333.333333333333],"xaxis":"x","y":[1481.4814814814813],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=archers<br>Damage x Size / Maintenance Cost=%{x}<br>Toughness x Size / Maintenance Cost=%{y}<extra></extra>","hovertext":["Metsänvartija","Nile Archers","Vigmen","Bush Hunters","Ballistrai","Longbowmen"],"legendgroup":"archers","marker":{"color":"#FFA15A","symbol":"circle"},"mode":"markers","name":"archers","orientation":"v","showlegend":true,"type":"scatter","x":[4545.454545454545,4545.454545454545,2727.272727272727,4545.454545454545,3888.8888888888887,2777.777777777778],"xaxis":"x","y":[2121.212121212121,2121.212121212121,3030.30303030303,1818.181818181818,1222.2222222222222,1111.111111111111],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=pikemen<br>Damage x Size / Maintenance Cost=%{x}<br>Toughness x Size / Maintenance Cost=%{y}<extra></extra>","hovertext":["Skoutatoi","Zupin Spearmen","Bondi"],"legendgroup":"pikemen","marker":{"color":"#19d3f3","symbol":"circle"},"mode":"markers","name":"pikemen","orientation":"v","showlegend":true,"type":"scatter","x":[2222.222222222222,2666.666666666667,2333.3333333333335],"xaxis":"x","y":[2626.2626262626263,2666.666666666667,3000],"yaxis":"y"},{"hovertemplate":"<b>%{hovertext}</b><br><br>Type=light infantry<br>Damage x Size / Maintenance Cost=%{x}<br>Toughness x Size / Maintenance Cost=%{y}<extra></extra>","hovertext":["Shomer","Guinean Uplanders","Horn Warriors","Abudrar"],"legendgroup":"light infantry","marker":{"color":"#FF6692","symbol":"circle"},"mode":"markers","name":"light infantry","orientation":"v","showlegend":true,"type":"scatter","x":[2222.222222222222,3333.333333333333,2666.6666666666665,2469.135802469136],"xaxis":"x","y":[5333.333333333333,2592.5925925925926,3555.5555555555557,1975.3086419753085],"yaxis":"y"}], {"height":height,"legend":{"title":{"text":"Type"},"tracegroupgap":0},"shapes":[{"opacity":0.5,"type":"line","x0":0,"x1":5000,"xref":"x","y0":0,"y1":5866.666666666667,"yref":"y"}],"template":{"data":{"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"heatmap"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermap":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermap"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]],"sequentialminus":[[0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","title":{"standoff":15},"zerolinecolor":"#283442","zerolinewidth":2}}},"title":{"text":"Damage vs. Toughness Trade-off per Gold"},"width":final_width,"xaxis":{"anchor":"y","domain":[0,1],"title":{"text":"Damage x Size / Maintenance Cost"}},"yaxis":{"anchor":"x","domain":[0,1],"title":{"text":"Toughness x Size / Maintenance Cost"}}});

	};
</script>

<svelte:head>
    <script src="https://cdn.plot.ly/plotly-2.20.0.min.js" charset="utf-8" onload={renderPlotly}></script>
</svelte:head>

<div class="jupyter">
	<div class="input input-md"><span class="heading"><h1 id="crusader-king-iii-man-at-arms-analysis">Crusader King III Man-at-Arms analysis<a href="#crusader-king-iii-man-at-arms-analysis"> ¶</a></h1></span>
<span class="heading"><h3 id="about-crusader-kings">About Crusader Kings<a href="#about-crusader-kings"> ¶</a></h3></span>
<p>I am a big fan of optimization. This extends into many aspects of my life, including recreation. Because of this, I am big fan of min-maxing in video games, and one of my favorites is a game called <a href="https://store.steampowered.com/app/1158310/Crusader_Kings_III/">Crusader Kings III</a>.</p>
<p>In CK3 you control a dynasty throughout the Middle Ages, playing as your ruler until they die, and then continuing as their heir. There is no real goal, besides making sure you always have an heir. Despite not having an explicit goal, generally you want a strong military to support both the defense of your realm and the conquest of others.</p>
<span class="heading"><h3 id="military-overview">Military Overview<a href="#military-overview"> ¶</a></h3></span>
<p>In CK3 there are two main types of military, levies and Man-at-Arms (MaA). Levies are essentially peasants drafted to fight, whereas MaA are trained soldiers that cost gold to both recruit and maintain, even when unraised. Basically, levies are cannon fodder and MaAs are what win you battles. There are also seige MaA, but they arent used in battle and therefore out of the scope of this analysis.</p>
<p>There are 6 main types of damaging MaA,which are:</p>
<ul>
<li>Light Infantry</li>
<li>Heavy Infantry</li>
<li>Pikemen</li>
<li>Light Horsemen</li>
<li>Heavy Horsemen</li>
<li>Archers</li>
</ul>
<p>each with their own strengths and weaknesses. There is a countering system ( Light Infantry &gt; Heavy Infantry &gt; Pikemen &gt; Horsemen &gt; Archer &gt; Light Infantry) but countering becomes less effective as the number of one type of unit increases (i.e. 100 archers effectively counter 100 light infantry, but 100 archers fail to counter 1,000 light infantry.) This drop-off in countering effectiveness means when facing the game's AI you can effectively build only one type of unit and be safe from countering.</p>
<p>Each MaA also potentially has terrain bonuses or weaknesses (ex. horsemen generally perform worse in mountainous terrain). This generally is only important if your domain is located in an area that is predominantly one type of terrain. Otherwise, general performance is more important.</p>
<p>Each MaA has a unit size, which is 100 soldiers per unit for all but a few types of MaA (Heavy Calavry, Elephant Cavalry, and a few other outliers).</p>
<p>Finally, and most importantly, each MaA has 4 battle stats and a cost and upkeep:</p>
<ul>
<li><strong>Damage</strong>: How much damage a soldier deals during the battle phase</li>
<li><strong>Toughness</strong>: How much damage a soldier can take before dying/retreating</li>
<li><strong>Pursuit</strong>: How much damage a soldier deals against retreating enemies (retreat phase)</li>
<li><strong>Screen</strong>: How much damage a soldier can block while retreating (retreat phase)</li>
<li><strong>Cost</strong>: How much gold it takes to train one unit of the MaA</li>
<li><strong>Upkeep</strong>: How much gold it takes to maintain the unit (raised and unraised)</li>
</ul>
<p>Each MaA has different values for each of these stats, and these are what make the real difference in a battle.</p>
<span class="heading"><h3 id="the-problem">The Problem<a href="#the-problem"> ¶</a></h3></span>
<p>There are 38 MaAs that are tied to different cultural traditions in the game. The goal of this analysis is to figure out which is the best, to guide the player in wisely choosing these traditions to grant access to the best MaA.</p></div><div class="input input-md"><span class="heading"><h2 id="getting-started">Getting started<a href="#getting-started"> ¶</a></h2></span>
<p>First we need to get the data for all the MaAs we are interested in comparing. This data can be conveniently found on the <a href="https://ck3.paradoxwikis.com/Army#Traditional">CK3 wiki</a>. Let's grab the data using pandas. We use selenium since the webpage will throw errors with javascript disabled.</p></div><div class="input input-code"><pre class="language-python"><code class="language-python"><span class="token keyword">import</span> time
<span class="token keyword">from</span> io <span class="token keyword">import</span> StringIO
<span class="token keyword">from</span> selenium <span class="token keyword">import</span> webdriver
<span class="token keyword">from</span> selenium<span class="token punctuation">.</span>webdriver<span class="token punctuation">.</span>chrome<span class="token punctuation">.</span>options <span class="token keyword">import</span> Options
<span class="token keyword">import</span> pandas <span class="token keyword">as</span> pd
<span class="token keyword">from</span> IPython<span class="token punctuation">.</span>display <span class="token keyword">import</span> display<span class="token punctuation">,</span> HTML
<span class="token keyword">import</span> rich

<span class="token comment"># Display helper function to hide index</span>
<span class="token keyword">def</span> <span class="token function">show_df</span><span class="token punctuation">(</span>df<span class="token punctuation">)</span><span class="token punctuation">:</span>
    display<span class="token punctuation">(</span>HTML<span class="token punctuation">(</span>df<span class="token punctuation">.</span>to_html<span class="token punctuation">(</span>index<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">)</span>

<span class="token comment"># Get dataframe from the webpage</span>
options <span class="token operator">=</span> Options<span class="token punctuation">(</span><span class="token punctuation">)</span>
driver <span class="token operator">=</span> webdriver<span class="token punctuation">.</span>Chrome<span class="token punctuation">(</span>options<span class="token operator">=</span>options<span class="token punctuation">)</span>
url <span class="token operator">=</span> <span class="token string">"https://ck3.paradoxwikis.com/Army"</span>
driver<span class="token punctuation">.</span>get<span class="token punctuation">(</span>url<span class="token punctuation">)</span>
html <span class="token operator">=</span> driver<span class="token punctuation">.</span>page_source
driver<span class="token punctuation">.</span>quit<span class="token punctuation">(</span><span class="token punctuation">)</span></code></pre></div><div class="input input-code"><pre class="language-python"><code class="language-python">df_list <span class="token operator">=</span> pd<span class="token punctuation">.</span>read_html<span class="token punctuation">(</span>StringIO<span class="token punctuation">(</span>html<span class="token punctuation">)</span><span class="token punctuation">)</span>
df <span class="token operator">=</span> df_list<span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">]</span> <span class="token comment"># We want the third table on the page</span>
df<span class="token punctuation">.</span>style<span class="token punctuation">.</span>hide<span class="token punctuation">(</span>axis<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">)</span>
show_df<span class="token punctuation">(</span>df<span class="token punctuation">[</span><span class="token punctuation">:</span><span class="token number">10</span><span class="token punctuation">]</span><span class="token punctuation">)</span></code></pre></div><table border="1" class="">
  <thead class="">
    <tr style="text-align: right;" class="">
      <th class="">Regiment</th>
      <th class="">Type</th>
      <th class="">Cost</th>
      <th class="">Raised maintenance</th>
      <th class="">Provisions used</th>
      <th class="">Unnamed: 5</th>
      <th class="">Unnamed: 6</th>
      <th class="">Unnamed: 7</th>
      <th class="">Unnamed: 8</th>
      <th class="">Counters</th>
      <th class="">Favorable terrain</th>
      <th class="">Unfavorable terrain</th>
      <th class="">Tradition</th>
      <th class="">Era</th>
    </tr>
  </thead>
  <tbody class="">
    <tr class="">
      <td class="">Abudrar</td>
      <td class="">NaN</td>
      <td class="">81.0</td>
      <td class="">0.81</td>
      <td class="">3</td>
      <td class="">20</td>
      <td class="">16</td>
      <td class="">20</td>
      <td class="">10</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Mountain Herding</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Ayyar</td>
      <td class="">NaN</td>
      <td class="">75.0</td>
      <td class="">1.08</td>
      <td class="">12</td>
      <td class="">35</td>
      <td class="">22</td>
      <td class="">12</td>
      <td class="">0</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Futuwaa</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Bush Hunters</td>
      <td class="">NaN</td>
      <td class="">55.0</td>
      <td class="">0.66</td>
      <td class="">3</td>
      <td class="">30</td>
      <td class="">12</td>
      <td class="">5</td>
      <td class="">0</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Bush Hunting</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Druzhina</td>
      <td class="">NaN</td>
      <td class="">117.0</td>
      <td class="">1.56</td>
      <td class="">7</td>
      <td class="">40</td>
      <td class="">30</td>
      <td class="">0</td>
      <td class="">30</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Druzhina</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Gendarmes</td>
      <td class="">NaN</td>
      <td class="">240.0</td>
      <td class="">2.52</td>
      <td class="">21</td>
      <td class="">125</td>
      <td class="">40</td>
      <td class="">20</td>
      <td class="">10</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Chanson de Geste</td>
      <td class="">Late Medieval</td>
    </tr>
    <tr class="">
      <td class="">Goedendag Militia</td>
      <td class="">NaN</td>
      <td class="">45.0</td>
      <td class="">0.45</td>
      <td class="">3</td>
      <td class="">13</td>
      <td class="">18</td>
      <td class="">0</td>
      <td class="">16</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Polders</td>
      <td class="">Late Medieval</td>
    </tr>
    <tr class="">
      <td class="">Guinean Uplanders</td>
      <td class="">NaN</td>
      <td class="">54.0</td>
      <td class="">0.54</td>
      <td class="">3</td>
      <td class="">18</td>
      <td class="">14</td>
      <td class="">0</td>
      <td class="">20</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Upland Skirmishing</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Horn Warriors</td>
      <td class="">NaN</td>
      <td class="">45.0</td>
      <td class="">0.45</td>
      <td class="">7</td>
      <td class="">12</td>
      <td class="">16</td>
      <td class="">0</td>
      <td class="">20</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Mountain Skirmishing</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Horse Archers</td>
      <td class="">NaN</td>
      <td class="">135.0</td>
      <td class="">1.35</td>
      <td class="">7</td>
      <td class="">45</td>
      <td class="">20</td>
      <td class="">40</td>
      <td class="">30</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Horse Lords</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Huscarls</td>
      <td class="">NaN</td>
      <td class="">115.0</td>
      <td class="">1.53</td>
      <td class="">3</td>
      <td class="">40</td>
      <td class="">26</td>
      <td class="">0</td>
      <td class="">24</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">NaN</td>
      <td class="">Hirds / Coastal Warriors</td>
      <td class="">Tribal</td>
    </tr>
  </tbody>
</table><div class="input input-md"><span class="heading"><h3 id="cleaning">Cleaning<a href="#cleaning"> ¶</a></h3></span>
<p>Now that we have the data, we have to clean up a couple of things. First let's add the proper column names.</p></div><div class="input input-code"><pre class="language-python"><code class="language-python">df<span class="token punctuation">.</span>rename<span class="token punctuation">(</span>columns<span class="token operator">=</span><span class="token punctuation">{'{'}</span><span class="token string">"Unnamed: 5"</span><span class="token punctuation">:</span> <span class="token string">"Damage"</span><span class="token punctuation">,</span> <span class="token string">"Unnamed: 6"</span> <span class="token punctuation">:</span> <span class="token string">"Toughness"</span><span class="token punctuation">,</span> <span class="token string">"Unnamed: 7"</span> <span class="token punctuation">:</span> <span class="token string">"Pursuit"</span><span class="token punctuation">,</span> <span class="token string">"Unnamed: 8"</span> <span class="token punctuation">:</span> <span class="token string">"Screen"</span><span class="token punctuation">{'}'}</span><span class="token punctuation">,</span> inplace<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span>
df<span class="token punctuation">.</span>columns</code></pre></div><pre class="output output-text">Index(['Regiment', 'Type', 'Cost', 'Raised maintenance', 'Provisions used',
       'Damage', 'Toughness', 'Pursuit', 'Screen', 'Counters',
       'Favorable terrain', 'Unfavorable terrain', 'Tradition', 'Era'],
      dtype='object')</pre><div class="input input-md"><p>Now let's fix the NaN values. For the purposes of this analysis we do not care about counters, favorable terrain, or unfavorable terrain, so we can drop those columns. However, we need the unit type for the unit size. To do this I will just manually input the unit sizes in the Type column.</p></div><div class="input input-code"><pre class="language-python"><code class="language-python"><span class="token comment"># drop NaN columns we don't need</span>
df<span class="token punctuation">.</span>drop<span class="token punctuation">(</span>columns<span class="token operator">=</span><span class="token punctuation">[</span><span class="token string">"Counters"</span><span class="token punctuation">,</span> <span class="token string">"Favorable terrain"</span><span class="token punctuation">,</span> <span class="token string">"Unfavorable terrain"</span><span class="token punctuation">]</span><span class="token punctuation">,</span> inplace<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></code></pre></div><div class="input input-code"><pre class="language-python"><code class="language-python">unit_types <span class="token operator">=</span> <span class="token punctuation">{'{'}</span>
    <span class="token string">"Abudrar"</span><span class="token punctuation">:</span> <span class="token string">'light infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Akritai"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Ayrudzi"</span><span class="token punctuation">:</span> <span class="token string">'light cavalry'</span><span class="token punctuation">,</span>
    <span class="token string">"Ayyar"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Ballistrai"</span><span class="token punctuation">:</span> <span class="token string">'archers'</span><span class="token punctuation">,</span>
    <span class="token string">"Bondi"</span><span class="token punctuation">:</span> <span class="token string">'pikemen'</span><span class="token punctuation">,</span>
    <span class="token string">"Bush Hunters"</span><span class="token punctuation">:</span> <span class="token string">'archers'</span><span class="token punctuation">,</span>
    <span class="token string">"Conrois"</span><span class="token punctuation">:</span> <span class="token string">'heavy cavalry'</span><span class="token punctuation">,</span>
    <span class="token string">"Druzhina"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Gendarmes"</span><span class="token punctuation">:</span> <span class="token string">'heavy cavalry'</span><span class="token punctuation">,</span>
    <span class="token string">"Goedendag Militia"</span><span class="token punctuation">:</span> <span class="token string">'light infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Guinean Uplanders"</span><span class="token punctuation">:</span> <span class="token string">'light infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Horn Warriors"</span><span class="token punctuation">:</span> <span class="token string">'light infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Horse Archers"</span><span class="token punctuation">:</span> <span class="token string">'horse archers'</span><span class="token punctuation">,</span>
    <span class="token string">"Huscarls"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Kataphraktoi"</span><span class="token punctuation">:</span> <span class="token string">'heavy cavalry'</span><span class="token punctuation">,</span>
    <span class="token string">"Khandayat"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Konni"</span><span class="token punctuation">:</span> <span class="token string">'light cavalry'</span><span class="token punctuation">,</span>
    <span class="token string">"Lenkas"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Longbowmen"</span><span class="token punctuation">:</span> <span class="token string">'archers'</span><span class="token punctuation">,</span>
    <span class="token string">"Metsänvartija"</span><span class="token punctuation">:</span> <span class="token string">'archers'</span><span class="token punctuation">,</span>
    <span class="token string">"Monaspa"</span><span class="token punctuation">:</span> <span class="token string">'heavy cavalry'</span><span class="token punctuation">,</span>
    <span class="token string">"Mountaineers"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Mubarizun"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Mulathanūm"</span><span class="token punctuation">:</span> <span class="token string">'light cavalry'</span><span class="token punctuation">,</span>
    <span class="token string">"Nile Archers"</span><span class="token punctuation">:</span> <span class="token string">'archers'</span><span class="token punctuation">,</span>
    <span class="token string">"Palace Guards"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Picchieri"</span><span class="token punctuation">:</span> <span class="token string">'pikemen'</span><span class="token punctuation">,</span>
    <span class="token string">"Sarawit"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Schiltron"</span><span class="token punctuation">:</span> <span class="token string">'pikemen'</span><span class="token punctuation">,</span>
    <span class="token string">"Shomer"</span><span class="token punctuation">:</span> <span class="token string">'light infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Skoutatoi"</span><span class="token punctuation">:</span> <span class="token string">'pikemen'</span><span class="token punctuation">,</span>
    <span class="token string">"Tarkhans"</span><span class="token punctuation">:</span> <span class="token string">'heavy cavalry'</span><span class="token punctuation">,</span>
    <span class="token string">"Tawashi"</span><span class="token punctuation">:</span> <span class="token string">'light cavalry'</span><span class="token punctuation">,</span>
    <span class="token string">"Varangian Veterans"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Vigmen"</span><span class="token punctuation">:</span> <span class="token string">'archers'</span><span class="token punctuation">,</span>
    <span class="token string">"Zbrojnosh"</span><span class="token punctuation">:</span> <span class="token string">'heavy infantry'</span><span class="token punctuation">,</span>
    <span class="token string">"Zupin Spearmen"</span><span class="token punctuation">:</span> <span class="token string">'pikemen'</span>
<span class="token punctuation">{'}'}</span>

unit_sizes <span class="token operator">=</span> <span class="token punctuation">{'{'}</span>
    <span class="token string">"Abudrar"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Akritai"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Ayrudzi"</span><span class="token punctuation">:</span> <span class="token number">50</span><span class="token punctuation">,</span>
    <span class="token string">"Ayyar"</span><span class="token punctuation">:</span> <span class="token number">50</span><span class="token punctuation">,</span>
    <span class="token string">"Ballistrai"</span><span class="token punctuation">:</span> <span class="token number">50</span><span class="token punctuation">,</span>
    <span class="token string">"Bondi"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Bush Hunters"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Conrois"</span><span class="token punctuation">:</span> <span class="token number">50</span><span class="token punctuation">,</span>
    <span class="token string">"Druzhina"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Gendarmes"</span><span class="token punctuation">:</span> <span class="token number">50</span><span class="token punctuation">,</span>
    <span class="token string">"Goedendag Militia"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Guinean Uplanders"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Horn Warriors"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Horse Archers"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Huscarls"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Kataphraktoi"</span><span class="token punctuation">:</span> <span class="token number">50</span><span class="token punctuation">,</span>
    <span class="token string">"Khandayat"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Konni"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Lenkas"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Longbowmen"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Metsänvartija"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Monaspa"</span><span class="token punctuation">:</span> <span class="token number">50</span><span class="token punctuation">,</span>
    <span class="token string">"Mountaineers"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Mubarizun"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Mulathanūm"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Nile Archers"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Palace Guards"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Picchieri"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Sarawit"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Schiltron"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Shomer"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Skoutatoi"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Tarkhans"</span><span class="token punctuation">:</span> <span class="token number">50</span><span class="token punctuation">,</span>
    <span class="token string">"Tawashi"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Varangian Veterans"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Vigmen"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Zbrojnosh"</span><span class="token punctuation">:</span> <span class="token number">100</span><span class="token punctuation">,</span>
    <span class="token string">"Zupin Spearmen"</span><span class="token punctuation">:</span> <span class="token number">100</span>
<span class="token punctuation">{'}'}</span>

df<span class="token punctuation">[</span><span class="token string">'Type'</span><span class="token punctuation">]</span> <span class="token operator">=</span> df<span class="token punctuation">[</span><span class="token string">'Regiment'</span><span class="token punctuation">]</span><span class="token punctuation">.</span><span class="token builtin">map</span><span class="token punctuation">(</span>unit_types<span class="token punctuation">)</span>
df<span class="token punctuation">[</span><span class="token string">'Size'</span><span class="token punctuation">]</span> <span class="token operator">=</span> df<span class="token punctuation">[</span><span class="token string">'Regiment'</span><span class="token punctuation">]</span><span class="token punctuation">.</span><span class="token builtin">map</span><span class="token punctuation">(</span>unit_sizes<span class="token punctuation">)</span>
show_df<span class="token punctuation">(</span>df<span class="token punctuation">[</span><span class="token punctuation">:</span><span class="token number">10</span><span class="token punctuation">]</span><span class="token punctuation">)</span></code></pre></div><table border="1" class="">
  <thead class="">
    <tr style="text-align: right;" class="">
      <th class="">Regiment</th>
      <th class="">Type</th>
      <th class="">Cost</th>
      <th class="">Raised maintenance</th>
      <th class="">Provisions used</th>
      <th class="">Damage</th>
      <th class="">Toughness</th>
      <th class="">Pursuit</th>
      <th class="">Screen</th>
      <th class="">Tradition</th>
      <th class="">Era</th>
      <th class="">Size</th>
    </tr>
  </thead>
  <tbody class="">
    <tr class="">
      <td class="">Abudrar</td>
      <td class="">light infantry</td>
      <td class="">81.0</td>
      <td class="">0.81</td>
      <td class="">3</td>
      <td class="">20</td>
      <td class="">16</td>
      <td class="">20</td>
      <td class="">10</td>
      <td class="">Mountain Herding</td>
      <td class="">Tribal</td>
      <td class="">100</td>
    </tr>
    <tr class="">
      <td class="">Ayyar</td>
      <td class="">heavy infantry</td>
      <td class="">75.0</td>
      <td class="">1.08</td>
      <td class="">12</td>
      <td class="">35</td>
      <td class="">22</td>
      <td class="">12</td>
      <td class="">0</td>
      <td class="">Futuwaa</td>
      <td class="">Tribal</td>
      <td class="">50</td>
    </tr>
    <tr class="">
      <td class="">Bush Hunters</td>
      <td class="">archers</td>
      <td class="">55.0</td>
      <td class="">0.66</td>
      <td class="">3</td>
      <td class="">30</td>
      <td class="">12</td>
      <td class="">5</td>
      <td class="">0</td>
      <td class="">Bush Hunting</td>
      <td class="">Tribal</td>
      <td class="">100</td>
    </tr>
    <tr class="">
      <td class="">Druzhina</td>
      <td class="">heavy infantry</td>
      <td class="">117.0</td>
      <td class="">1.56</td>
      <td class="">7</td>
      <td class="">40</td>
      <td class="">30</td>
      <td class="">0</td>
      <td class="">30</td>
      <td class="">Druzhina</td>
      <td class="">Tribal</td>
      <td class="">100</td>
    </tr>
    <tr class="">
      <td class="">Gendarmes</td>
      <td class="">heavy cavalry</td>
      <td class="">240.0</td>
      <td class="">2.52</td>
      <td class="">21</td>
      <td class="">125</td>
      <td class="">40</td>
      <td class="">20</td>
      <td class="">10</td>
      <td class="">Chanson de Geste</td>
      <td class="">Late Medieval</td>
      <td class="">50</td>
    </tr>
    <tr class="">
      <td class="">Goedendag Militia</td>
      <td class="">light infantry</td>
      <td class="">45.0</td>
      <td class="">0.45</td>
      <td class="">3</td>
      <td class="">13</td>
      <td class="">18</td>
      <td class="">0</td>
      <td class="">16</td>
      <td class="">Polders</td>
      <td class="">Late Medieval</td>
      <td class="">100</td>
    </tr>
    <tr class="">
      <td class="">Guinean Uplanders</td>
      <td class="">light infantry</td>
      <td class="">54.0</td>
      <td class="">0.54</td>
      <td class="">3</td>
      <td class="">18</td>
      <td class="">14</td>
      <td class="">0</td>
      <td class="">20</td>
      <td class="">Upland Skirmishing</td>
      <td class="">Tribal</td>
      <td class="">100</td>
    </tr>
    <tr class="">
      <td class="">Horn Warriors</td>
      <td class="">light infantry</td>
      <td class="">45.0</td>
      <td class="">0.45</td>
      <td class="">7</td>
      <td class="">12</td>
      <td class="">16</td>
      <td class="">0</td>
      <td class="">20</td>
      <td class="">Mountain Skirmishing</td>
      <td class="">Tribal</td>
      <td class="">100</td>
    </tr>
    <tr class="">
      <td class="">Horse Archers</td>
      <td class="">horse archers</td>
      <td class="">135.0</td>
      <td class="">1.35</td>
      <td class="">7</td>
      <td class="">45</td>
      <td class="">20</td>
      <td class="">40</td>
      <td class="">30</td>
      <td class="">Horse Lords</td>
      <td class="">Tribal</td>
      <td class="">100</td>
    </tr>
    <tr class="">
      <td class="">Huscarls</td>
      <td class="">heavy infantry</td>
      <td class="">115.0</td>
      <td class="">1.53</td>
      <td class="">3</td>
      <td class="">40</td>
      <td class="">26</td>
      <td class="">0</td>
      <td class="">24</td>
      <td class="">Hirds / Coastal Warriors</td>
      <td class="">Tribal</td>
      <td class="">100</td>
    </tr>
  </tbody>
</table><div class="input input-md"><span class="heading"><h2 id="analysis">Analysis<a href="#analysis"> ¶</a></h2></span>
<p>Now that the data clean we can get to the analysis. Firstly, let's look at what the most effective MaA is for winning battles with no consideration for maintenance or what happens in the retreat phase. There are a few things we must first note:</p>
<ul>
<li>Damage: During a battle, there are several rounds until one side is entirely routed. During each of these round, 1 soldier does 0.03 damage per point of Damage stat.</li>
<li>Toughness: Each point allows for a soldier to take 1 total damage before routing.</li>
<li>Combat Width: An extra consideration is something called combat width, computed with the equation (Enemy units + Ally units) * (0.5 * Terrain Width). This gives an advantage to smaller unit sizes in a head to head. For the purposes of this analysis we will assume the terrain width is 1.</li>
</ul>
<p>These will come in handy later, but initially let's just look at damage * toughness * unit size</p>
<span class="heading"><h4 id="era-considerations">Era considerations<a href="#era-considerations"> ¶</a></h4></span>
<p>Since some MaAs only become available much later into the game, they have zero utility for most of a play-through. Because of this I will limit the comparisons to only tribal era MaAs, which are always available to be recruited.</p></div><div class="input input-code"><pre class="language-python"><code class="language-python">df <span class="token operator">=</span> df<span class="token punctuation">[</span>df<span class="token punctuation">.</span>Era <span class="token operator">==</span> <span class="token string">'Tribal'</span><span class="token punctuation">]</span><span class="token punctuation">.</span>copy<span class="token punctuation">(</span><span class="token punctuation">)</span>
df<span class="token punctuation">[</span><span class="token string">'Era'</span><span class="token punctuation">]</span><span class="token punctuation">.</span>value_counts<span class="token punctuation">(</span><span class="token punctuation">)</span></code></pre></div><pre class="output output-text">Era
Tribal    33
Name: count, dtype: int64</pre><div class="input input-md"><span class="heading"><h4 id="damage-x-toughness-x-size">Damage x Toughness x Size<a href="#damage-x-toughness-x-size"> ¶</a></h4></span></div><div class="input input-code"><pre class="language-python"><code class="language-python">df<span class="token punctuation">[</span><span class="token string">'d*t*s'</span><span class="token punctuation">]</span> <span class="token operator">=</span> df<span class="token punctuation">[</span><span class="token string">'Damage'</span><span class="token punctuation">]</span> <span class="token operator">*</span> df<span class="token punctuation">[</span><span class="token string">'Toughness'</span><span class="token punctuation">]</span> <span class="token operator">*</span> df<span class="token punctuation">[</span><span class="token string">'Size'</span><span class="token punctuation">]</span>
df<span class="token punctuation">.</span>sort_values<span class="token punctuation">(</span>by<span class="token operator">=</span><span class="token string">'d*t*s'</span><span class="token punctuation">,</span> ascending<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">,</span> inplace<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span>

show_df<span class="token punctuation">(</span>df<span class="token punctuation">.</span>loc<span class="token punctuation">[</span><span class="token punctuation">:</span><span class="token punctuation">,</span><span class="token punctuation">[</span><span class="token string">'Regiment'</span><span class="token punctuation">,</span> <span class="token string">'Type'</span><span class="token punctuation">,</span> <span class="token string">'d*t*s'</span><span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">[</span><span class="token punctuation">:</span><span class="token number">10</span><span class="token punctuation">]</span><span class="token punctuation">)</span></code></pre></div><table border="1" class="">
  <thead class="">
    <tr style="text-align: right;" class="">
      <th class="">Regiment</th>
      <th class="">Type</th>
      <th class="">d*t*s</th>
    </tr>
  </thead>
  <tbody class="">
    <tr class="">
      <td class="">Kataphraktoi</td>
      <td class="">heavy cavalry</td>
      <td class="">210000</td>
    </tr>
    <tr class="">
      <td class="">Tarkhans</td>
      <td class="">heavy cavalry</td>
      <td class="">165000</td>
    </tr>
    <tr class="">
      <td class="">Monaspa</td>
      <td class="">heavy cavalry</td>
      <td class="">165000</td>
    </tr>
    <tr class="">
      <td class="">Varangian Veterans</td>
      <td class="">heavy infantry</td>
      <td class="">135000</td>
    </tr>
    <tr class="">
      <td class="">Conrois</td>
      <td class="">heavy cavalry</td>
      <td class="">125000</td>
    </tr>
    <tr class="">
      <td class="">Druzhina</td>
      <td class="">heavy infantry</td>
      <td class="">120000</td>
    </tr>
    <tr class="">
      <td class="">Mubarizun</td>
      <td class="">heavy infantry</td>
      <td class="">112500</td>
    </tr>
    <tr class="">
      <td class="">Mountaineers</td>
      <td class="">heavy infantry</td>
      <td class="">104000</td>
    </tr>
    <tr class="">
      <td class="">Huscarls</td>
      <td class="">heavy infantry</td>
      <td class="">104000</td>
    </tr>
    <tr class="">
      <td class="">Lenkas</td>
      <td class="">heavy infantry</td>
      <td class="">92400</td>
    </tr>
  </tbody>
</table><div class="input input-md"><p>Well, there's the top 10, but let's see if we can get a better sense of the distribution.</p></div><div class="input input-code"><pre class="language-python"><code class="language-python"><span class="token keyword">import</span> plotly<span class="token punctuation">.</span>express <span class="token keyword">as</span> px
<span class="token keyword">from</span> plotly<span class="token punctuation">.</span>colors <span class="token keyword">import</span> named_colorscales

fig <span class="token operator">=</span> px<span class="token punctuation">.</span>strip<span class="token punctuation">(</span>
    df<span class="token punctuation">,</span> 
    y<span class="token operator">=</span><span class="token string">"d*t*s"</span><span class="token punctuation">,</span> 
    hover_name<span class="token operator">=</span><span class="token string">'Regiment'</span><span class="token punctuation">,</span> 
    hover_data<span class="token operator">=</span><span class="token punctuation">[</span><span class="token string">'Type'</span><span class="token punctuation">,</span> <span class="token string">'Size'</span><span class="token punctuation">]</span><span class="token punctuation">,</span> 
    labels<span class="token operator">=</span><span class="token punctuation">{'{'}</span><span class="token string">'d*t*s'</span><span class="token punctuation">:</span> <span class="token string">'Damage x Toughness x Size'</span><span class="token punctuation">{'}'}</span><span class="token punctuation">,</span>
    title<span class="token operator">=</span><span class="token string">"Most Effective MaA in CK3"</span><span class="token punctuation">,</span> 
    height<span class="token operator">=</span><span class="token number">600</span><span class="token punctuation">,</span> 
    width<span class="token operator">=</span><span class="token number">800</span><span class="token punctuation">,</span> 
    template<span class="token operator">=</span><span class="token string">'plotly_dark'</span><span class="token punctuation">,</span> 
    color<span class="token operator">=</span><span class="token string">'Type'</span>
<span class="token punctuation">)</span>
<span class="token comment"># fig.update_traces(marker_color="yellow")</span>
fig<span class="token punctuation">.</span>show<span class="token punctuation">(</span><span class="token punctuation">)</span></code></pre></div><div class="output"><figure id="plotly_14_0" class="output"></figure></div><div class="input input-md"><p>We can see that the top contenders are all heavy cavalry, even before taking into account the combat width advantage they have for having a smaller unit size.</p>
<p>This shows Kataphraktoi as our top performer by Damage x Toughness x Size.</p>
<span class="heading"><h4 id="damage-x-size-vs-toughness-x-size">Damage x Size vs. Toughness x Size<a href="#damage-x-size-vs-toughness-x-size"> ¶</a></h4></span>
<p>There are some instances, however, where Toughness or Damage may be more or less preferable than the other. For example, if you are running an army with a lot of levies (cannon fodder), toughness is less important since more of the enemy's damage is soaked up by your levies. Conversely, if you are running a Knight heavy army (Knights are special characters, not nameless troops), toughness may be more important to protect your relatively fragile but high damage knights. Let's look at a scatter plot comparing damage and toughness.</p></div><div class="input input-code"><pre class="language-python"><code class="language-python"><span class="token keyword">import</span> plotly<span class="token punctuation">.</span>graph_objects <span class="token keyword">as</span> go

df<span class="token punctuation">[</span><span class="token string">'t*s'</span><span class="token punctuation">]</span> <span class="token operator">=</span> df<span class="token punctuation">[</span><span class="token string">'Toughness'</span><span class="token punctuation">]</span> <span class="token operator">*</span> df<span class="token punctuation">[</span><span class="token string">'Size'</span><span class="token punctuation">]</span>
df<span class="token punctuation">[</span><span class="token string">'d*s'</span><span class="token punctuation">]</span> <span class="token operator">=</span> df<span class="token punctuation">[</span><span class="token string">'Damage'</span><span class="token punctuation">]</span> <span class="token operator">*</span> df<span class="token punctuation">[</span><span class="token string">'Size'</span><span class="token punctuation">]</span>
fig <span class="token operator">=</span> px<span class="token punctuation">.</span>scatter<span class="token punctuation">(</span>
    df<span class="token punctuation">,</span> 
    x<span class="token operator">=</span><span class="token string">'d*s'</span><span class="token punctuation">,</span> 
    y<span class="token operator">=</span><span class="token string">'t*s'</span><span class="token punctuation">,</span> 
    labels<span class="token operator">=</span><span class="token punctuation">{'{'}</span><span class="token string">'d*s'</span><span class="token punctuation">:</span><span class="token string">"Damage x Size"</span><span class="token punctuation">,</span> <span class="token string">'t*s'</span><span class="token punctuation">:</span> <span class="token string">'Toughness x Size'</span><span class="token punctuation">{'}'}</span><span class="token punctuation">,</span>
    title<span class="token operator">=</span><span class="token string">'Damage vs. Toughness Trade-off'</span><span class="token punctuation">,</span>
    hover_name<span class="token operator">=</span><span class="token string">'Regiment'</span><span class="token punctuation">,</span>
    color<span class="token operator">=</span><span class="token string">'Type'</span><span class="token punctuation">,</span> 
    height<span class="token operator">=</span><span class="token number">600</span><span class="token punctuation">,</span> 
    width<span class="token operator">=</span><span class="token number">800</span><span class="token punctuation">,</span>
    template<span class="token operator">=</span><span class="token string">'plotly_dark'</span><span class="token punctuation">)</span>

fig<span class="token punctuation">.</span>add_shape<span class="token punctuation">(</span>
    <span class="token builtin">type</span><span class="token operator">=</span><span class="token string">'line'</span><span class="token punctuation">,</span>
    xref<span class="token operator">=</span><span class="token string">'x'</span><span class="token punctuation">,</span>
    yref<span class="token operator">=</span><span class="token string">'y'</span><span class="token punctuation">,</span>
    x0<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">,</span>
    y0<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">,</span>
    x1<span class="token operator">=</span>df<span class="token punctuation">[</span><span class="token string">'d*s'</span><span class="token punctuation">]</span><span class="token punctuation">.</span><span class="token builtin">max</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">*</span><span class="token number">1.1</span><span class="token punctuation">,</span>
    y1<span class="token operator">=</span>df<span class="token punctuation">[</span><span class="token string">'t*s'</span><span class="token punctuation">]</span><span class="token punctuation">.</span><span class="token builtin">max</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">*</span><span class="token number">1.1</span><span class="token punctuation">,</span>
    opacity<span class="token operator">=</span><span class="token number">0.5</span>
<span class="token punctuation">)</span>

fig<span class="token punctuation">.</span>show<span class="token punctuation">(</span><span class="token punctuation">)</span></code></pre></div><div class="output"><figure id="plotly_16_0" class="output"></figure></div><div class="input input-md"><p>This paints a slightly more nuanced picture. Now it seems like there are two main contenders for "best" depending on what the player is prioritizing. This now shows Varangian Veterans as the best if the player prefers toughness, and Kataphraktoi if the player prefers damage, based on the rest of their army composition.</p>
<span class="heading"><h4 id="on-pursuit-and-screen">On Pursuit and Screen<a href="#on-pursuit-and-screen"> ¶</a></h4></span>
<p>Pursuit is how much extra damage can be done after winning a battle. This can be useful for what is called "stack-wiping," which is when you kill or capture the entire enemy army, with no one able to escape. While this can be very useful it requires winning the battle first. Therefore, I will not be considering it in these analyses. Similarly, screen is only useful when you have lost a battle to protect from further loses. Our goal is to not lose any battles, so we will not be considering it in these analyses either.</p>
<span class="heading"><h3 id="gold-considerations">Gold Considerations<a href="#gold-considerations"> ¶</a></h3></span>
<p>MaA cost gold to recruit, and to maintain. The cost to recruit is a one time cost, and only really matter in the very early game, since once recruited you will never have to pay that cost again. For this reason, we will not consider it in these analyses. Maintenance, however, is important for much longer. There are severe penalties for fighting battles while in debt, and a massive army of the most expensive troops can lead a player to financial ruin very quickly. In the late game maintenance is less of a concern since your economy should be strong enough to support any army, but for much of the game this is still an important consideration. Lets look at the same two graphs as before, but now weighted by maintenance costs.</p></div><div class="input input-code"><pre class="language-python"><code class="language-python">df<span class="token punctuation">[</span><span class="token string">'d*t*s/gold'</span><span class="token punctuation">]</span> <span class="token operator">=</span> df<span class="token punctuation">[</span><span class="token string">'d*t*s'</span><span class="token punctuation">]</span> <span class="token operator">/</span> df<span class="token punctuation">[</span><span class="token string">'Raised maintenance'</span><span class="token punctuation">]</span>
df<span class="token punctuation">.</span>sort_values<span class="token punctuation">(</span>by<span class="token operator">=</span><span class="token string">'d*t*s/gold'</span><span class="token punctuation">,</span> ascending<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">,</span> inplace<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span>
show_df<span class="token punctuation">(</span>df<span class="token punctuation">.</span>loc<span class="token punctuation">[</span><span class="token punctuation">:</span><span class="token punctuation">,</span><span class="token punctuation">[</span><span class="token string">'Regiment'</span><span class="token punctuation">,</span> <span class="token string">'Type'</span><span class="token punctuation">,</span> <span class="token string">'Raised maintenance'</span><span class="token punctuation">,</span><span class="token string">'d*t*s/gold'</span><span class="token punctuation">,</span> <span class="token string">'Era'</span><span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token punctuation">[</span><span class="token punctuation">:</span><span class="token number">10</span><span class="token punctuation">]</span><span class="token punctuation">)</span></code></pre></div><table border="1" class="">
  <thead class="">
    <tr style="text-align: right;" class="">
      <th class="">Regiment</th>
      <th class="">Type</th>
      <th class="">Raised maintenance</th>
      <th class="">d*t*s/gold</th>
      <th class="">Era</th>
    </tr>
  </thead>
  <tbody class="">
    <tr class="">
      <td class="">Mubarizun</td>
      <td class="">heavy infantry</td>
      <td class="">1.44</td>
      <td class="">78125.000000</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Kataphraktoi</td>
      <td class="">heavy cavalry</td>
      <td class="">2.73</td>
      <td class="">76923.076923</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Druzhina</td>
      <td class="">heavy infantry</td>
      <td class="">1.56</td>
      <td class="">76923.076923</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Mountaineers</td>
      <td class="">heavy infantry</td>
      <td class="">1.44</td>
      <td class="">72222.222222</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Ayrudzi</td>
      <td class="">light cavalry</td>
      <td class="">1.05</td>
      <td class="">71428.571429</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Conrois</td>
      <td class="">heavy cavalry</td>
      <td class="">1.78</td>
      <td class="">70224.719101</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Huscarls</td>
      <td class="">heavy infantry</td>
      <td class="">1.53</td>
      <td class="">67973.856209</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Varangian Veterans</td>
      <td class="">heavy infantry</td>
      <td class="">2.00</td>
      <td class="">67500.000000</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Horse Archers</td>
      <td class="">horse archers</td>
      <td class="">1.35</td>
      <td class="">66666.666667</td>
      <td class="">Tribal</td>
    </tr>
    <tr class="">
      <td class="">Khandayat</td>
      <td class="">heavy infantry</td>
      <td class="">1.44</td>
      <td class="">64166.666667</td>
      <td class="">Tribal</td>
    </tr>
  </tbody>
</table><div class="input input-md"><p>This changes up the top 10 quite a bit. With cost considerations heavy infantry MaAs are now preferable, with Mubarizun coming out on top. Let's look at the strip chart.</p></div><div class="input input-code"><pre class="language-python"><code class="language-python">fig <span class="token operator">=</span> px<span class="token punctuation">.</span>strip<span class="token punctuation">(</span>
    df<span class="token punctuation">,</span> 
    y<span class="token operator">=</span><span class="token string">"d*t*s/gold"</span><span class="token punctuation">,</span> 
    hover_name<span class="token operator">=</span><span class="token string">'Regiment'</span><span class="token punctuation">,</span> 
    hover_data<span class="token operator">=</span><span class="token punctuation">[</span><span class="token string">'Type'</span><span class="token punctuation">,</span> <span class="token string">'Size'</span><span class="token punctuation">,</span> <span class="token string">'Raised maintenance'</span><span class="token punctuation">]</span><span class="token punctuation">,</span> 
    labels<span class="token operator">=</span><span class="token punctuation">{'{'}</span><span class="token string">'d*t*s/gold'</span><span class="token punctuation">:</span> <span class="token string">'(Damage x Toughness x Size) / Maintenance Cost'</span><span class="token punctuation">{'}'}</span><span class="token punctuation">,</span>
    title<span class="token operator">=</span><span class="token string">"Most Effective MaA in CK3 Per Gold"</span><span class="token punctuation">,</span> 
    height<span class="token operator">=</span><span class="token number">600</span><span class="token punctuation">,</span> 
    width<span class="token operator">=</span><span class="token number">800</span><span class="token punctuation">,</span> 
    template<span class="token operator">=</span><span class="token string">'plotly_dark'</span><span class="token punctuation">,</span> 
    color<span class="token operator">=</span><span class="token string">'Type'</span>
<span class="token punctuation">)</span>
<span class="token comment"># fig.update_traces(marker_color="yellow")</span>
fig<span class="token punctuation">.</span>show<span class="token punctuation">(</span><span class="token punctuation">)</span></code></pre></div><div class="output"><figure id="plotly_20_0" class="output"></figure></div><div class="input input-md"><p>We can see that the ranking are much more linear. There are some interesting outliers. For one, almost all the light cavalry is terrible, except the Ayrudzi. This is likely a balancing effort by the developers of the game to make light cavalry more attractive, since Ayrudzi are a recent addition. Another outlier is longbowmen, which are the lowest of the bunch. The reason for this is, unlike other MaAs, they improve with each era, becoming very formidable by the end of the game. Unfortunately as mentioned before, late game has limited utility since the player will likely already be very strong, and can field almost any force.</p>
<span class="heading"><h4 id="damage-vs-toughness-per-maintenance">Damage vs Toughness per Maintenance<a href="#damage-vs-toughness-per-maintenance"> ¶</a></h4></span>
<p>Now finally lets look at Damage and Toughness individually, while considering Maintenance.</p></div><div class="input input-code"><pre class="language-python"><code class="language-python">df<span class="token punctuation">[</span><span class="token string">'t*s/gold'</span><span class="token punctuation">]</span> <span class="token operator">=</span> df<span class="token punctuation">[</span><span class="token string">'t*s'</span><span class="token punctuation">]</span> <span class="token operator">/</span> df<span class="token punctuation">[</span><span class="token string">'Raised maintenance'</span><span class="token punctuation">]</span>
df<span class="token punctuation">[</span><span class="token string">'d*s/gold'</span><span class="token punctuation">]</span> <span class="token operator">=</span> df<span class="token punctuation">[</span><span class="token string">'d*s'</span><span class="token punctuation">]</span> <span class="token operator">/</span> df<span class="token punctuation">[</span><span class="token string">'Raised maintenance'</span><span class="token punctuation">]</span>
fig <span class="token operator">=</span> px<span class="token punctuation">.</span>scatter<span class="token punctuation">(</span>
    df<span class="token punctuation">,</span> 
    x<span class="token operator">=</span><span class="token string">'d*s/gold'</span><span class="token punctuation">,</span> 
    y<span class="token operator">=</span><span class="token string">'t*s/gold'</span><span class="token punctuation">,</span> 
    labels<span class="token operator">=</span><span class="token punctuation">{'{'}</span><span class="token string">'d*s/gold'</span><span class="token punctuation">:</span><span class="token string">"Damage x Size / Maintenance Cost"</span><span class="token punctuation">,</span> <span class="token string">'t*s/gold'</span><span class="token punctuation">:</span> <span class="token string">'Toughness x Size / Maintenance Cost'</span><span class="token punctuation">{'}'}</span><span class="token punctuation">,</span>
    title<span class="token operator">=</span><span class="token string">'Damage vs. Toughness Trade-off per Gold'</span><span class="token punctuation">,</span>
    hover_name<span class="token operator">=</span><span class="token string">'Regiment'</span><span class="token punctuation">,</span>
    color<span class="token operator">=</span><span class="token string">'Type'</span><span class="token punctuation">,</span> 
    height<span class="token operator">=</span><span class="token number">600</span><span class="token punctuation">,</span> 
    width<span class="token operator">=</span><span class="token number">800</span><span class="token punctuation">,</span>
    template<span class="token operator">=</span><span class="token string">'plotly_dark'</span><span class="token punctuation">)</span>

fig<span class="token punctuation">.</span>add_shape<span class="token punctuation">(</span>
    <span class="token builtin">type</span><span class="token operator">=</span><span class="token string">'line'</span><span class="token punctuation">,</span>
    xref<span class="token operator">=</span><span class="token string">'x'</span><span class="token punctuation">,</span>
    yref<span class="token operator">=</span><span class="token string">'y'</span><span class="token punctuation">,</span>
    x0<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">,</span>
    y0<span class="token operator">=</span><span class="token number">0</span><span class="token punctuation">,</span>
    x1<span class="token operator">=</span>df<span class="token punctuation">[</span><span class="token string">'d*s/gold'</span><span class="token punctuation">]</span><span class="token punctuation">.</span><span class="token builtin">max</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">*</span><span class="token number">1.1</span><span class="token punctuation">,</span>
    y1<span class="token operator">=</span>df<span class="token punctuation">[</span><span class="token string">'t*s/gold'</span><span class="token punctuation">]</span><span class="token punctuation">.</span><span class="token builtin">max</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">*</span><span class="token number">1.1</span><span class="token punctuation">,</span>
    opacity<span class="token operator">=</span><span class="token number">0.5</span>
<span class="token punctuation">)</span>

fig<span class="token punctuation">.</span>show<span class="token punctuation">(</span><span class="token punctuation">)</span></code></pre></div><div class="output"><figure id="plotly_22_0" class="output"></figure></div><div class="input input-md"><p>This paints an interesting picture. Our usual suspects (Heavy Cavalry and Heavy Infantry) aren't found on either extreme. Instead, we have two archers on the far right (Damage heavy per maintenance) and a single light infantry on the top (Toughness heavy per maintenance). None of the specialist appear in the top 10 damage x toughness charts, but may prove valuable if the player:</p>
<ol>
<li>Has very little income</li>
<li>Has a ton of levies (High damage preference) or Very strong Knights (High toughness preference)</li>
</ol>
<p>However, situation 1 and situation 2 very rarely happen together, since if you have a lot of levies or a lot of strong knights, you likely will have a lot of income too.</p>
<span class="heading"><h2 id="conclusion">Conclusion<a href="#conclusion"> ¶</a></h2></span>
<p>So, what does all of this mean? Essentially, it can be boiled down to these questions.</p>
<ol>
<li>Do you have a lot of extra income? If so max out on Kataphraktoi.</li>
<li>Do you have a good amount of extra income, but can't support a lot of Kataphraktoi? If so max out on Mubarizun.</li>
<li>Are you struggling with gold and can't support max stacks of Mubarizun or other comparable Heavy Infantry? If so Ayrzudi have the lowest maintenance in the Damage x Toughness / Gold top 10.</li>
<li>Are you struggling with gold but want a damage or toughness focused composition? Max out Nile archers for damage, or Shomer for toughness.</li>
</ol>
<span class="heading"><h2 id="further-work">Further work<a href="#further-work"> ¶</a></h2></span>
<p>I plan to come back to this and compute the optimal MaA for adventurers (who use provisions for maintenance, not gold), as well as to add a head-to-head simulation to better capture the effects of terrain width. Taking terrain width into account will boost up heavy cavalry more, and perhaps make them the best choice given a budget as well. Additionally, it would be interesting to do a pairwise 1v1 tournament to see who has the most wins and loses when considering unit type counters.</p></div> 
</div>

<style lang="scss">
/* Do Not Remove  */
/* Used to render latex math */
@import url('https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css');

.jupyter {
	width: 100%;
}

.plot-container {
	width: 100% !important;
}

.plotly {
	padding: 110px;
}

/* Link on hover */
.heading > * > a {
	visibility: hidden;
	text-decoration: none;
}
.heading:hover > * > a {
	visibility: visible;
}
div .heading > * > a:hover {
	color: rgb(69, 69, 255);
}

pre {
	margin: 0;
}

.heading {
	display: block;
	margin-top: 1em;
}

/* Controls all inputs */
.input {
	width: 100%;
	// background-color: oklch(var(--b3));
}

/* Controls the code blocks */
.input-code {
	margin-bottom: 1.5em;
	font-size: 0.95em;
	height:fit-content;
}

/* Controls the markdown blocks */
.input-md {
	// margin-top: 1.5em;
	margin-bottom: 1.5em;
	height: fit-content;
}

p {
	line-height: 1.5em;
	margin-top: 1em;
}

/* Controls all output blocks */
.output:not(figure) {
	display: block;
	margin: 16px;
	width: calc(100% - 32px);
	padding: 0em;
	overflow: auto;
	// border: 1px solid oklch(var(--b3));
	// background-color: oklch(var(--b3));
}

/* Controls stdout (print statements, text output) */
.output-text {
	font-size: 1em;
}

/* Controls Images */
img {
	max-width: 100%;
}

/* Controls plotly figures */
figure {
	max-width: 100%;
	width:100%;
	max-height: 100%;
	margin: 0px !important;
	display: block;
	
}

li {
	margin-top: 0;
	margin-bottom: 0;
}

/* Wrapper around table outputs */
.output-html-table {
	font-size: 0.85em;
}
/* Table formatting */
th {
	text-align: right;
	border: 0px;
	padding: 0.2em 0.5em;
	color: black;
}
td {
	text-align: right;
	border: 0px;
	padding: 0.2em 0.5em;
	color: black;
}
/* Table headings */
thead > tr > th {
	background-color: #ccc;
	border: 0px;
}
thead > tr:nth-child(2) > th {
	background-color: #ddd;
}
/* Highlight Every other row */
tr:nth-child(even) {
	background-color: #ddd;
}
/* Give rows a border */
tr {
	border: 1px solid #ddd;
}
table {
	border-collapse: collapse;
	justify-self: center;
	margin-right: auto;
	margin: 10px 0;
	display: block;
	width: max-content;
	max-width: 100%;
	overflow: auto;
	background: white;
}


</style>