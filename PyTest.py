
# www.metacode9.com


from ctypes import alignment
import numpy as np
import pandas as pd

import sys
import os
import plotly.offline as ply
# import plotly.express as ply
import plotly.graph_objs as go
# import plotly.express as px
import plotly.io as po


ply.offline.init_notebook_mode()

s_data = np.loadtxt('./gryo_data', dtype='str',delimiter=',')

df = pd.DataFrame(s_data, columns=['Time','GX','GY','GZ'])

x_time = np.arange(0, len(df[['Time']]), 0.1)
gx=list(map(float,df.GX))
gy=list(map(float,df.GY))
gz=list(map(float,df.GZ))

y_threshold = [0.3] * len(df.GX)


# Data
acc_x = go.Scatter( x=x_time, y=gx, name='Gx',
                    line = dict( color = 'blue', width = 1)
)
acc_y = go.Scatter( x=x_time, y=gy, name='Ay',
                    line = dict( color = 'red', width = 1)
)
acc_z = go.Scatter( x=x_time, y=gz, name='Az',
                    line = dict( color = 'green', width = 1)
)

data = [acc_x, acc_y, acc_z]

# Edit the layout
layout = dict(title = 'Gryo chart', alignment='center',
            xaxis = dict(title = 'Time'),
            yaxis = dict(title = 'Value'),
            )

fig = dict(data=data, layout=layout)
fig.update(layout_yaxis_range = [-2,2])


po.write_html(fig, file='gyro_chart.html', auto_open=True)






