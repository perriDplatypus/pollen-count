import axios, { type AxiosResponse } from 'axios'
import { load } from 'cheerio'

const pollenData = {
  date: '',
  pollen: 'high',
  asthma: 'low',
}

async function scrapeData() {
  const response = await axios.get('https://www.melbournepollen.com.au/')
  console.log(load(response.data))
  return true
}

export default scrapeData
