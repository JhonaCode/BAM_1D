###To the local and not local language in the data 
import locale

#pip install nc-time-axis
import nc_time_axis

params = {
 	  #'text.usetex': True,
 	  'figure.figsize': [8.6,4], # instead of 4.5, 4.5
	  #'text.latex.preamble': ['\usepackage{gensymb}'],
	  'font.family' : 'serif',
	  'font.sans-serif'    : 'Helvetica',#, Avant Garde, Computer Modern Sans serif
          'font.size' : 12,
          #dont work with latex
	  #'font.weight' : 'normal',
	  'font.weight' : 500,
	  'lines.linewidth':2,
	 #note that font.size controls default text sizes.  To configure
	# special text sizes tick labels, axes, labels, title, etc, see the rc
	# settings for axes and ticks. Special text sizes can be defined
	# relative to font.size, using the following values: xx-small, x-small,
	# small, medium, large, x-large, xx-large, larger, or smaller
 	  #'legend.fontsize': 'large',
 	  'legend.fontsize': 'medium',
 	  'axes.labelsize' : 'x-large',
 	  #'axes.labelweight' :'normal',
 	  'axes.labelweight' :'500',
 	  'xtick.labelsize': 'large',
 	  'ytick.labelsize': 'large',
          #'xtick.major.size': 4,      # major tick size in points
          #'xtick.major.size': 4,      # major tick size in points
          #'xtick.minor.size': 4,   # minor tick size in points
          #'xtick.major.pad': 4,      # distance to major tick label in points
          #'xtick.minor.pad': 4,      # distance to the minor tick label in points
          #'xtick.color': 'k',      # color of the tick labels
          'xtick.direction': 'out',     # direction: in or out
	  #'mathtext.bf'  : 'serif:bold'
        }

def axis_format(fig,ax):

    #TO put in english see Parameter to more information
    locale.setlocale(locale.LC_ALL, 'en_IN')

    #minor axis
    formatter = nc_time_axis.CFTimeFormatter("%d", "standard")
    locator   = nc_time_axis.NetCDFTimeDateLocator(15,"standard")
    ax.xaxis.set_minor_formatter(formatter)
    ax.xaxis.set_minor_locator(locator)

    # Set major
    locator=nc_time_axis.NetCDFTimeDateLocator(1,"standard")
    formatter = nc_time_axis.CFTimeFormatter("\n%b", "standard")
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)


    return fig,ax

