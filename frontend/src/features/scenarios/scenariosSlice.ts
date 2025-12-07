import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface Scenario {
  id: string
  name: string
  description: string
  status: 'draft' | 'active' | 'completed'
}

interface ScenariosState {
  scenarios: Scenario[]
  loading: boolean
}

const initialState: ScenariosState = {
  scenarios: [],
  loading: false,
}

const scenariosSlice = createSlice({
  name: 'scenarios',
  initialState,
  reducers: {
    setScenarios: (state, action: PayloadAction<Scenario[]>) => {
      state.scenarios = action.payload
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload
    },
  },
})

export const { setScenarios, setLoading } = scenariosSlice.actions
export default scenariosSlice.reducer
