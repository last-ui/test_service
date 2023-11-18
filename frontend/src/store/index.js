//import Vue from 'vue'
//import Vuex from 'vuex'
import { createStore } from 'vuex'

import { Picture } from '@/api/pictures'
import {
    ADD_PICTURE,
    REMOVE_PICTURE,
    SET_PICTURES
} from './mutation-types.js'

//Vue.use(Vuex)

// Состояние
const state = {
  pictures: []  // список картинок
}

// Геттеры
const getters = {
  pictures: state => state.pictures  // получаем список картинок из состояния
}

// Мутации
const mutations = {
  // Добавляем картинку в список
  [ADD_PICTURE] (state, picture) {
    state.pictures = [picture, ...state.pictures]
  },
  // Убираем картинку из списка
  [REMOVE_PICTURE] (state, { id }) {
    state.pictures = state.pictures.filter(picture => {
      return picture.id !== id
    })
  },
  // Задаем список картинок
  [SET_PICTURES] (state, { pictures }) {
    state.pictures = pictures
  }
}

// Действия
const actions = {
  createPicture ({ commit }, pictureData) {
    Picture.create(pictureData).then(picture => {
      commit(ADD_PICTURE, picture)
    })
  },
  deletePicture ({ commit }, picture) {
    Picture.delete(picture).then(response => {
      commit(REMOVE_PICTURE, picture)
    })
  },
  getPictures ({ commit }) {
    Picture.list().then(pictures => {
      commit(SET_PICTURES, { pictures })
    })
  }
}

export default createStore({
  state,
  getters,
  actions,
  mutations
}
)
