import { configureStore } from '@reduxjs/toolkit'
import authReducer from './auth/authSlice'
import scenariosReducer from './scenarios/scenariosSlice'
import vmsReducer from './vms/vmsSlice'
import uiReducer from './ui/uiSlice'

export const store = configureStore({
  reducer: {
    auth: authReducer,
    scenarios: scenariosReducer,
    vms: vmsReducer,
    ui: uiReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
