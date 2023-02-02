import {
  ArrowTable,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import {Box, Card, CardContent, Typography} from "@mui/material"
import TrendingDownIcon from '@mui/icons-material/TrendingDown';
import TrendingFlatIcon from '@mui/icons-material/TrendingFlat';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'
import { Line } from 'react-chartjs-2'
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

interface State {
}

interface Labels {
  x: string,
  y: string
}

type Datum = string|number|Date
type Data = Datum[]

const arrowTableToArray = (t: ArrowTable): Data => {
  const n = t.dataRows
  const res: Data = []
  for (let i = 1; i <= n; i++) {
    res.push(t.getCell(i, 1).content as Datum)
  }
  return res
}

const getMonthString = (month: number) => {
  if (month + 1 < 10) {
    return '0' + (month + 1).toString()
  } else {
    return (month + 1).toString()
  }
}

// Add segment in datasets options with borderColor with function (ctx: any) => changeColor(ctx, ...)
// const changeColor = (ctx: any, colorUpThresh: string, colorDownThresh: string, thresh: number) => {
//   if (ctx.p0.raw <= thresh && ctx.p1.raw <= thresh) {
//     return colorDownThresh
//   } else {
//     if (ctx.p0.raw > thresh && ctx.p1.raw > thresh) {
//       return colorUpThresh
//     } else {
//       return colorUpThresh
//     }
//   }
// }

const options = {
  responsive: true,
  plugins: {
    legend: {
      display: false
    },
  },
  scales: {
        x: {
          grid: {
            drawBorder: false,
          }
        },
        y: {
          grid: {
            display: false,
            drawBorder: false,
          }
        }
      }
}

const thresHoldDisplay = (thresh: number|null) => {
  if (thresh !== null) {
    return (
      <Typography
        sx={{
          fontWeight: "bold"
        }}
      >
        S = {thresh}
      </Typography>
    )
  } else {
    return (
      <Typography
        sx={{
          fontWeight: "bold"
        }}
      >
        S = Ø
      </Typography>
    )
  }
}

const tablesToData = (x: Data, y: Data, title: string, defaultColor: string, thresh: number|null, threshColor: string) => {
    let abs = []
    if (x[0] instanceof Date) {
      // @ts-ignore
      abs = x.map((date: Date) => `${date.getDate()}/${getMonthString(date.getMonth())}`)
    } else {
      abs = x
    }
    if (thresh == null) {
      const data = {
        "labels": abs,
        datasets: [
          {
            label: title,
            data: y,
            borderColor: defaultColor,
            backgroundColor: defaultColor,
            tension: 0.5,
            pointRadius: 2
          },
        ],
      }
      return data
    } else {
      const data = {
        "labels": abs,
        datasets: [
          {
            label: "Seuil",
            data: y.map((data: Datum) => thresh),
            borderColor: threshColor,
            backgroundColor: threshColor,
            borderWidth: 2,
            pointRadius: 0,
            pointHitRadius: 0
          },
          {
            label: title,
            data: y,
            borderColor: defaultColor,
            backgroundColor: defaultColor,
            tension: 0.5,
            pointRadius: 2
          },
        ],
      }
      return data
    }
  }

class StreamlitGraphicCard extends StreamlitComponentBase<State> {
  public state: State = {}
  private title: string = this.props.args["title"]
  private x: Data = arrowTableToArray(this.props.args["x"])
  private y: Data = arrowTableToArray(this.props.args["y"])
  private labels: Labels = this.props.args["labels"]
  private metrics = this.props.args["metrics"]
  private defaultColor: string = this.props.args["defaultColor"]
  private threshColor: string = this.props.args["threshColor"]
  private thresh: number|null = this.props.args["thresh"]
  private data = tablesToData(this.x, this.y, this.title, this.defaultColor, this.thresh, this.threshColor)

  public render = (): ReactNode => {

    return (
      <Box
        sx={{
          padding: 2,
        }}
      >
        <Card
          sx={{
            height: 250,
            width: 290
        }}
        >
          <CardContent>
            <Box>
              <Box
              sx={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center"
              }}
              >
                <Typography
                  sx={{
                    fontWeight: "bold"
                  }}
                >
                  {this.title}
                </Typography>
                {thresHoldDisplay(this.thresh)}
                <Typography
                  sx={{
                    fontWeight: "bold"
                  }}
                >
                  {this.labels["y"]}
                </Typography>
              </Box>
              <Box
                sx={{
                  marginTop: 2,
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center"
                }}
              >
                <Box
                  sx={{
                    display: "flex",
                    alignItems: "center"
                  }}
                >
                  <Typography
                    sx={{
                      marginLeft: 1,
                      fontWeight: "bold"
                    }}
                  >
                    min
                  </Typography>
                  <Typography
                  >
                    ={this.metrics["min"]}
                  </Typography>
                </Box>
                <Box
                  sx={{
                    display: "flex",
                    alignItems: "center"
                  }}
                >
                  <Typography
                    sx={{
                      marginLeft: 1,
                      fontWeight: "bold"
                    }}
                  >
                    x̄
                  </Typography>
                  <Typography
                  >
                    ={this.metrics["mean"]}
                  </Typography>
                </Box>
                <Box
                  sx={{
                    display: "flex",
                    alignItems: "center"
                  }}
                >
                  <Typography
                    sx={{
                      marginLeft: 1,
                      fontWeight: "bold"
                    }}
                  >
                    max
                  </Typography>
                  <Typography
                  >
                    ={this.metrics["max"]}
                  </Typography>
                </Box>
              </Box>
              <Box
                sx={{
                  marginTop: 2
                }}
              >
                <Line options={options} data={this.data}></Line>
              </Box>
            </Box>
          </CardContent>
        </Card>
      </Box>
    )
  }
}

export default withStreamlitConnection(StreamlitGraphicCard)
