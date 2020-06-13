import pandas as pd
import numpy as np
import geoviews as gv
import geoviews.tile_sources as gvts
from geoviews import dim, opts

import api

def draw(data):
    gv.extension('bokeh')

    df = pd.DataFrame (data, columns = ['mag','lng','lat','lokasyon','date'])
    
    earthquakes_gv_points = gv.Points(df, ['lng', 'lat'],
                                   ['lokasyon','mag','date'])
    
    
    gvts.CartoLight
    gvts.CartoLight * earthquakes_gv_points
    gvts.CartoLight.options(width=1000, height=800, xaxis=None, yaxis=None, show_grid=False)  * earthquakes_gv_points
    earthquakes_plot = (gvts.CartoLight * earthquakes_gv_points).opts(
        opts.Points(width=980, height=700, alpha=0.3,
                    xaxis=None, yaxis=None,
                    size=np.sqrt(dim('mag'))*20))
    
    
    earthquakes_plot = (gvts.CartoLight * earthquakes_gv_points).opts(
        opts.Points(width=980, height=700, alpha=0.3, hover_line_color='black',  
                    line_color='black', xaxis=None, yaxis=None,
                    tools=['hover'],size=np.sqrt(dim('mag'))*20))
    
    from bokeh.models import HoverTool
    tooltips = [('Magnitude', '@mag'),
                ('Date', '@date'),
                ('Location', '@lokasyon'),
                ('Longitude', '$x'),
                ('Latitude', '$y'),
                ]
    
    hover = HoverTool(tooltips=tooltips)
    
    earthquakes_plot = (gvts.CartoLight * earthquakes_gv_points).opts(
        opts.Points(width=980, height=700, alpha=0.3, hover_line_color='black',  
                    line_color='black', xaxis=None, yaxis=None,
                    tools=[hover],size=np.sqrt(dim('mag'))*20,
                    hover_fill_color=None, hover_fill_alpha=0.5))
    
    
    
    return (earthquakes_plot).opts(
        opts.Graph(edge_selection_line_color='black', edge_hover_line_color='red',
                   edge_line_width=1, edge_line_alpha=0.01, edge_nonselection_line_alpha=0.01,
                   width=800, height=600))

earthquakes = api.getDatasFromAPI({"date": "2020-01-01","limit":"100"})
draw(earthquakes)
