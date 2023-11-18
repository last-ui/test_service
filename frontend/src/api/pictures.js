import { HTTP } from './common'
export const Picture = {
  create (config) {
    return HTTP.post('/pictures/', config).then(response => {
      return response.data
    })
  },
  delete (picture) {
    return HTTP.delete(`/pictures/${picture.id}/`)
  },
  list () {
    return HTTP.get('/pictures/').then(response => {
      return response.data
    })
  }
}
