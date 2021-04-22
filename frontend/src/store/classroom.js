import api from "../api"

export default {
  state: {
    currentCourse: null,
  },
  mutations: {
    setCourse(state, course) {
      state.currentCourse = course
    }
  },
  actions: {
    async setCourse({ commit, getters }, courseId) {
      if (getters.currentCourse?.id == courseId)
        return
      commit('setCourse', null)
      api.get('/enrolled-courses/'+courseId)
      .then(course => commit('setCourse', course))
    }
  },
  getters: {
    currentCourse(state) {
      return state.currentCourse
    }
  }
}
