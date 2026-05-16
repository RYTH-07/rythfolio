
code = '''import { Component, ReactNode } from "react";

interface Props { children: ReactNode; fallback?: ReactNode; }
interface State { hasError: boolean; }

export default class ErrorBoundary extends Component<Props, State> {
  state = { hasError: false };
  static getDerivedStateFromError() { return { hasError: true }; }
  render() {
    if (this.state.hasError) return this.props.fallback ?? null;
    return this.props.children;
  }
}'''
with open('src/app/components/ErrorBoundary.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('ErrorBoundary done!')
